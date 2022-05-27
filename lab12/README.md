# Batch processing using Apache Spark

In this laboratory you will perform simple batch processing tasks using Apache Spark and examine Spark's execution plans and DAGs.

## Setup 

1. Start VPN session, log in into your virtual machine and install docker:


```bash
scp lab12.ipynb stXXX@stXXXvm101.rtb-lab.pl:
ssh stXXX@stXXXvm101.rtb-lab.pl
sudo apt install -y docker.io
```

2. Copy sample dataset and Jupyter Notebook for this lab:

```bash
mkdir ~/ext
cd ~/ext
mv ../lab12.ipynb . 

wget https://github.com/RTBHOUSE/mimuw-lab/releases/download/pre-lab12/lab12_dataset.tar.gz
tar xf lab12_dataset.tar.gz && rm lab12_dataset.tar.gz
```

3. Start Jupyter Lab:

```bash
sudo docker pull jupyter/pyspark-notebook
sudo docker run -it --network=host -v`pwd`:/ext -w /ext jupyter/pyspark-notebook
```

4. Connect to Jupyter Lab using a web browser.

Use link displayed in the console output, e.g. http://stXXXvmXXX.rtb-lab.pl:8888/lab?token=TOKEN

5. Open `lab12.ipybn`.
