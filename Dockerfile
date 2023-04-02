FROM ucsdets/datahub-base-notebook

USER root

RUN apt-get -y install htop

WORKDIR /app

ENV DISPLAY=:0

ENTRYPOINT ["jupyter", "notebook", "--allow-root"]
