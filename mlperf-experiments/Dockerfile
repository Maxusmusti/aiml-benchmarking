FROM pytorch/pytorch:latest

COPY run_peft.py ./run_peft.py
#COPY ds_zero3_cpu.yaml ds_zero3_cpu.yaml
COPY requirements.txt ./requirements.txt 
COPY exemplars-raw ./exemplars-raw

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV CUDA_VISIBLE_DEVICES=0
