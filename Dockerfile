FROM python:3

RUN pip3 install coverage

ADD blackjack.py /

CMD [ "python", "./blackjack.py" ]