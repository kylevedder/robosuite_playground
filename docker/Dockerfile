FROM kylevedder/cudagl:11.7.1-devel-ubuntu20.04
SHELL ["/bin/bash", "-c"]
# Set the timezone info because otherwise tzinfo blocks install 
# flow and ignores the non-interactive frontend command 🤬🤬🤬
RUN ln -snf /usr/share/zoneinfo/America/New_York /etc/localtime && echo "/usr/share/zoneinfo/America/New_York" > /etc/timezone

# Core system packages
RUN apt update --fix-missing
RUN apt install -y software-properties-common wget curl gpg gcc git make apt-utils

# Install miniconda to /miniconda
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}

# Set standard environment variables so any libraries with CUDA support build with CUDA 
# support for all the common NVidia architectures
ENV TORCH_CUDA_ARCH_LIST="Ampere;Turing;Pascal"
ENV FORCE_CUDA="1"
RUN conda update -y conda
RUN conda install numpy python pytorch==1.13 torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia -y
RUN pip install open3d==0.16

RUN git clone https://github.com/ARISE-Initiative/robosuite.git /robosuite
WORKDIR /robosuite
RUN git checkout eb01e1ffa46f1af0a3aa3ac363d5e63097a6cbcc
RUN pip install -r requirements.txt

RUN conda install termcolor h5py gymnasium
RUN pip install stable-baselines3[extra]


# Add the project to the PYTHONPATH so that we can import modules from it
ENV PYTHONPATH=/project:${PYTHONPATH}
# Add the modified bashrc to the container so we get a nice prompt and persistent history
COPY bashrc /root/.bashrc
# Set the working directory to the project directory, where we will mount the repo
WORKDIR /project