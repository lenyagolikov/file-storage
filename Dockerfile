FROM snakepacker/python:all as builder

RUN python3.10 -m venv /usr/share/python3/venv \
    && /usr/share/python3/venv/bin/pip install -U pip

COPY requirements.txt /mnt/
RUN /usr/share/python3/venv/bin/pip install -Ur /mnt/requirements.txt

COPY . /mnt/
RUN /usr/share/python3/venv/bin/pip install /mnt/

FROM snakepacker/python:3.10 as base

COPY --from=builder /usr/share/python3/venv /usr/share/python3/venv
RUN ln -snf /usr/share/python3/venv/bin/app* /usr/local/bin/

ADD store /store

ADD scripts/start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]
