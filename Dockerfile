FROM python:alpine
WORKDIR /WordFrequencyAnalysis
COPY . /WordFrequencyAnalysis
RUN pip install nltk
#RUN python -m nltk.downloader stopwords
CMD [ "python", "./WordFrequencyAnalysis.py"]