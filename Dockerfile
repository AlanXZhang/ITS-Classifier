FROM ucsdets/datahub-base-notebook

USER root

RUN apt-get -y install htop

WORKDIR /app

ENV DISPLAY=:0

ENTRYPOINT ["jupyter", "notebook", "--allow-root"]

RUN pip install --upgrade tensorflow==2.10.0

RUN pip install transformers==4.22.1

RUN pip install -U scikit-learn

RUN pip install nltk

RUN pip install matplotlib

RUN pip install plotly

RUN pip install seaborn

RUN pip install markupsafe==2.0.1
