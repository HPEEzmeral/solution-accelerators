FROM python:3.12

WORKDIR /workspace

ADD src/requirements.txt /workspace/requirements.txt
RUN pip install -r requirements.txt

ADD src/app.py src/theme.py src/chain.py src/prompts.py src/INFO.md /workspace/

ENV HOME=/workspace

EXPOSE 7860

CMD ["python3", "-u", "/workspace/app.py"]