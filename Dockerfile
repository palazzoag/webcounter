FROM python:3.10-alpine
LABEL description="python_webcounter"
LABEL version="1.0.0"
LABEL maintainer="cfreire@cfreire.com.pt"

ARG REDIS_URL='localhost'
ENV REDIS_URL=${REDIS_URL}

ARG CI_COMMIT_SHORT_SHA='develop'
ENV CI_COMMIT_SHORT_SHA=${CI_COMMIT_SHORT_SHA}

EXPOSE 5000

RUN adduser -D user
USER user
WORKDIR /home/user
ENV PATH="/home/user/.local/bin:${PATH}"

COPY --chown=user:user requirements.txt requirements.txt
RUN pip install --user -r requirements.txt
COPY --chown=user:user . .

CMD ["python", "app.py"]