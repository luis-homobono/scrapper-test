FROM ubuntu:22.04

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update -y && apt-get install -y curl gnupg wget nano
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install --fix-missing
RUN apt-get install -y google-chrome-stable
RUN apt-get install -y python3-pip

RUN mkdir /var/www/
WORKDIR /var/www

# INSTALL DRIVER CHROME
# RUN apt-get install -yqq unzip
# RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
# RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

COPY . .

RUN pip install --upgrade pip
RUN pip install -Ur requirements.txt


EXPOSE 5001
CMD ["/bin/bash"]
# CMD [ "flask", "run", "--reload" ]