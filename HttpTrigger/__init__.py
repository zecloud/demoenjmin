import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if req.method == 'POST':
        return func.HttpResponse(
            "plop",
            status_code=200,
            mimetype="text/plain"
        )
    else:
        return func.HttpResponse(
            "This function only accepts POST requests.",
            status_code=405
        )