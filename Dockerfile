FROM python:3.11.3

ENV HOME_DIR = /opt/pbot

RUN pip install --upgrade pip && pip install pipenv
RUN adduser pbot

USER pbot
WORKDIR $HOME_DIR
COPY --chown=pbot:pbot . /$HOME_DIR
RUN pip install --user -r requirements.txt && pipenv install

EXPOSE 5000
ENTRYPOINT [ "python", "./personal_helper/run_bot.py"]
