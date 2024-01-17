import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="learnmodule_text")
def learnmodule_text(req: func.HttpRequest) -> func.HttpResponse:
    import logging
    logging.info('learnmodule_text: start')

    import requests
    import markdownify
    import re
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin

    url = req.params.get('url')
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')

    logging.info(f'learnmodule_text: fetching url: {url}')

    if url:
        responseText = ""
        responseModule = requests.get(url)
        logging.info(f'learnmodule_text: GET HTTP status code: {responseModule.status_code}')

        if responseModule.status_code == 200:
            logging.info(f'learnmodule_text: parsing content')
            contentModule = responseModule.text
            soupMain = BeautifulSoup(contentModule, "html.parser")

            logging.info(f'learnmodule_text: finding all links')
            links = soupMain.find_all(class_="unit-title")
            absolute_urls = [urljoin(url, link["href"]) for link in links]

            for absolute_url in absolute_urls:
                logging.info(f'learnmodule_text: fetching url: {absolute_url}')
                learnUnit = requests.get(absolute_url)
                logging.info(f'learnmodule_text: GET HTTP status code: {learnUnit.status_code}')
                if learnUnit.status_code == 200:
                    logging.info(f'learnmodule_text: parsing content')
                    soupLearnUnit = BeautifulSoup(learnUnit.text, "html.parser")
                    divUnitInnerSection = soupLearnUnit.find(id="unit-inner-section")
                    if divUnitInnerSection:
                        skipUnit = False

                        for h1 in divUnitInnerSection.find_all("h1", class_="margin-right-xxl-desktop"):
                            h1text = h1.get_text().lower()

                            if "exercise" in h1text or ("check" in h1text and "knowledge" in h1text) or "summary" in h1text:
                                skipUnit = True
                        
                        for ul in divUnitInnerSection.find_all("ul", class_="metadata"):
                            ul.decompose()
                        for d in divUnitInnerSection.find_all("div", class_="xp-tag"):
                            d.decompose()
                        for next in divUnitInnerSection.find_all("div", id="next-section"):
                            next.decompose()
                        for img in divUnitInnerSection.find_all("img"):
                            img.decompose()
                        for code in divUnitInnerSection.find_all("code"):
                            code.decompose()

                        logging.info(f'learnmodule_text: trasnforming to markdown')

                        learnUnitContent = markdownify.markdownify(str(divUnitInnerSection), heading_style="ATX", bullets="-")
                        learnUnitContent = re.sub('\n{3,}', '\n\n', learnUnitContent)

                        if not skipUnit:
                            responseText = responseText + "\n" + learnUnitContent
        else:
           logging.info(f'learnmodule_text: Could not parse the learn module with URL {url}')
           return func.HttpResponse(
             f"Could not parse the learn module with URL {url}",
             status_code=200
        ) 

        logging.info(f'learnmodule_text: done')

        return func.HttpResponse(responseText, status_code=200)
    else:
        return func.HttpResponse(
             "Pass a learn module URL in the query string or in the request body to fetch the text.",
             status_code=200
        )

@app.route(route="learnarticle_text")
def learnarticle_text(req: func.HttpRequest) -> func.HttpResponse:
    import logging
    logging.info('learnarticle_text: start')

    import requests
    import markdownify
    import re
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin

    url = req.params.get('url')
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')

    logging.info(f'learnarticle_text: fetching url: {url}')

    if url:
        responseText = ""
        responseModule = requests.get(url)
        logging.info(f'learnarticle_text: GET HTTP status code: {responseModule.status_code}')

        if responseModule.status_code == 200:
            logging.info(f'learnarticle_text: parsing content')
            contentModule = responseModule.text
            soupMain = BeautifulSoup(contentModule, "html.parser")

            divUnitInnerSection = soupMain.find("div", class_="content")
            
            for el in divUnitInnerSection.find_all("div", class_="page-metadata-container"):
                el.decompose()
            for el in divUnitInnerSection.find_all("nav", id="center-doc-outline"):
                el.decompose()
            for code in divUnitInnerSection.find_all("code"):
                code.decompose()

                        
            logging.info(f'learnarticle_text: trasnforming to markdown')

            learnUnitContent = markdownify.markdownify(str(divUnitInnerSection), heading_style="ATX", bullets="-")
            learnUnitContent = re.sub('\n{3,}', '\n\n', learnUnitContent)
            responseText = learnUnitContent

        else:
           logging.info(f'learnarticle_text: Could not parse the learn module with URL {url}')
           return func.HttpResponse(
             f"Could not parse the learn module with URL {url}",
             status_code=200
        ) 

        logging.info(f'learnarticle_text: done')

        return func.HttpResponse(responseText, status_code=200)
    else:
        return func.HttpResponse(
             "Pass a learn article URL in the query string or in the request body to fetch the text.",
             status_code=200
        )