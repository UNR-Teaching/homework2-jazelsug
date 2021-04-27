FROM python:3

ADD blackjack.py /

CMD [ "python", "./blackjack.py" ]