FROM python:3.9

RUN pip install pipenv

COPY Pipfile Pipfile.lock *.py /

RUN pipenv install --system --deploy

ENTRYPOINT [ "python", "netbox_gen.py" ]