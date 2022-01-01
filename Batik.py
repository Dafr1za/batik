{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Salinan dari neural_network.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Dafr1za/Batik/blob/main/Batik.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HbEtzsONCbXH",
        "outputId": "8a3bdebe-803a-4800-8b99-a88c39150c38"
      },
      "source": [
        "# Download dataset\n",
        "!wget --no-check-certificate \\\n",
        "    https://drive.google.com/file/d/1qFtbQzNZTlL-d9wSwrB5DjDZKFTYLdZ0/view?usp=sharing \\\n",
        "    -O /tmp/Batik.zip"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--2021-12-31 05:48:04--  https://drive.google.com/file/d/1qFtbQzNZTlL-d9wSwrB5DjDZKFTYLdZ0/view?usp=sharing\n",
            "Resolving drive.google.com (drive.google.com)... 173.194.210.113, 173.194.210.102, 173.194.210.138, ...\n",
            "Connecting to drive.google.com (drive.google.com)|173.194.210.113|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: unspecified [text/html]\n",
            "Saving to: ‘/tmp/Batik.zip’\n",
            "\n",
            "/tmp/Batik.zip          [ <=>                ]  65.18K  --.-KB/s    in 0.003s  \n",
            "\n",
            "2021-12-31 05:48:05 (25.0 MB/s) - ‘/tmp/Batik.zip’ saved [66744]\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lEbqHHtWCcZi",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 380
        },
        "outputId": "bb79aa3d-a778-422f-d22b-ba14a9fef0ee"
      },
      "source": [
        "import os\n",
        "import zipfile\n",
        "from google.colab import drive\n",
        "\n",
        "drive.mount('/content/drive/')\n",
        "\n",
        "zip_ref = zipfile.ZipFile(\"/content/drive/My Drive/Colab Notebooks/Batik.zip\", 'r')\n",
        "zip_ref.extractall(\"/tmp\")\n",
        "zip_ref.close()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "MessageError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mMessageError\u001b[0m                              Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-7-ecf96d959539>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mgoogle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcolab\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mdrive\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0mdrive\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmount\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'/content/drive/'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0mzip_ref\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mzipfile\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mZipFile\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"/content/drive/My Drive/Colab Notebooks/Batik.zip\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'r'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/google/colab/drive.py\u001b[0m in \u001b[0;36mmount\u001b[0;34m(mountpoint, force_remount, timeout_ms, use_metadata_server)\u001b[0m\n\u001b[1;32m    111\u001b[0m       \u001b[0mtimeout_ms\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtimeout_ms\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    112\u001b[0m       \u001b[0muse_metadata_server\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0muse_metadata_server\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 113\u001b[0;31m       ephemeral=ephemeral)\n\u001b[0m\u001b[1;32m    114\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    115\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/google/colab/drive.py\u001b[0m in \u001b[0;36m_mount\u001b[0;34m(mountpoint, force_remount, timeout_ms, use_metadata_server, ephemeral)\u001b[0m\n\u001b[1;32m    134\u001b[0m   \u001b[0;32mif\u001b[0m \u001b[0mephemeral\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    135\u001b[0m     _message.blocking_request(\n\u001b[0;32m--> 136\u001b[0;31m         'request_auth', request={'authType': 'dfs_ephemeral'}, timeout_sec=None)\n\u001b[0m\u001b[1;32m    137\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    138\u001b[0m   \u001b[0mmountpoint\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_os\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexpanduser\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmountpoint\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/google/colab/_message.py\u001b[0m in \u001b[0;36mblocking_request\u001b[0;34m(request_type, request, timeout_sec, parent)\u001b[0m\n\u001b[1;32m    173\u001b[0m   request_id = send_request(\n\u001b[1;32m    174\u001b[0m       request_type, request, parent=parent, expect_reply=True)\n\u001b[0;32m--> 175\u001b[0;31m   \u001b[0;32mreturn\u001b[0m \u001b[0mread_reply_from_input\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrequest_id\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout_sec\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/google/colab/_message.py\u001b[0m in \u001b[0;36mread_reply_from_input\u001b[0;34m(message_id, timeout_sec)\u001b[0m\n\u001b[1;32m    104\u001b[0m         reply.get('colab_msg_id') == message_id):\n\u001b[1;32m    105\u001b[0m       \u001b[0;32mif\u001b[0m \u001b[0;34m'error'\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mreply\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 106\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mMessageError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mreply\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'error'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    107\u001b[0m       \u001b[0;32mreturn\u001b[0m \u001b[0mreply\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'data'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    108\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mMessageError\u001b[0m: Error: credential propagation was unsuccessful"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qTUcSDf2CeBY"
      },
      "source": [
        "base_dir = '/tmp/Batik'\n",
        "\n",
        "train_dir = os.path.join(base_dir, 'train')\n",
        "validation_dir = os.path.join(base_dir, 'validation')\n",
        "\n",
        "train_cats_dir = os.path.join(train_dir, 'batik-ceplok')\n",
        "train_dogs_dir = os.path.join(train_dir, 'batik-parang')\n",
        "\n",
        "validation_cats_dir = os.path.join(validation_dir, 'batik-ceplok')\n",
        "validation_dogs_dir = os.path.join(validation_dir, 'batik-parang')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4KUVPIfRCfw0",
        "outputId": "48327f48-a473-448b-e3cb-5a368d419cf7"
      },
      "source": [
        "# Cek penamaan image yang ada di folder train_cats_dir dan train_dogs_dir\n",
        "print(os.listdir(train_cats_dir)[:10])\n",
        "print(os.listdir(train_dogs_dir)[:10])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['46.jpg', '9.jpg', '3.jpg', '25.jpg', '24.jpg', '7.jpg', '4.jpg', '29.jpg', '13.jpg', '38.jpg']\n",
            "['9.jpg', '16.jpg', '15.jpg', '3.jpg', '7.jpg', '4.jpg', '13.jpg', '21.jpg', '18.jpg', '2.jpg']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dAsPl9g3Chr2",
        "outputId": "384eae0c-fa00-4349-fd45-04e3f10cb89d"
      },
      "source": [
        "# Cek jumlah data train dan data validation\n",
        "print('total training cat images:', len(os.listdir(train_cats_dir)))\n",
        "print('total training dog images:', len(os.listdir(train_dogs_dir)))\n",
        "print('total validation cat images:', len(os.listdir(validation_cats_dir)))\n",
        "print('total validation dog images:', len(os.listdir(validation_dogs_dir)))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "total training cat images: 21\n",
            "total training dog images: 20\n",
            "total validation cat images: 21\n",
            "total validation dog images: 20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 252
        },
        "id": "fFVUUI8bCoAv",
        "outputId": "1f6c5435-c460-43d4-9f9d-09c5dcd00723"
      },
      "source": [
        "# Tampilkan 8 image per kelas dengan ukuran 4x4 \n",
        "\n",
        "%matplotlib inline\n",
        "\n",
        "import matplotlib.pyplot as plt\n",
        "import matplotlib.image as mpimg\n",
        "\n",
        "nrows = 4\n",
        "ncols = 4\n",
        "\n",
        "pic_index = 0\n",
        "\n",
        "fig = plt.gcf()\n",
        "fig.set_size_inches(ncols * 4, nrows * 4)\n",
        "\n",
        "pic_index += 8\n",
        "next_cat_pix = [os.path.join(train_cats_dir, fname) \n",
        "                for fname in os.listdir(train_cats_dir)[pic_index-8:pic_index]]\n",
        "next_dog_pix = [os.path.join(train_dogs_dir, fname) \n",
        "                for fname in os.listdir(train_dogs_dir)[pic_index-8:pic_index]]\n",
        "\n",
        "for i, img_path in enumerate(next_cat_pix+next_dog_pix):\n",
        "  # Set up subplot; subplot indices start at 1\n",
        "  sp = plt.subplot(nrows, ncols, i + 1)\n",
        "  sp.axis('Off') # Don't show axes (or gridlines)\n",
        "\n",
        "  img = mpimg.imread(img_path)\n",
        "  plt.imshow(img)\n",
        "\n",
        "plt.show()\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-8-83bef0146054>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     16\u001b[0m \u001b[0mpic_index\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;36m8\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     17\u001b[0m next_cat_pix = [os.path.join(train_cats_dir, fname) \n\u001b[0;32m---> 18\u001b[0;31m                 for fname in os.listdir(train_cats_dir)[pic_index-8:pic_index]]\n\u001b[0m\u001b[1;32m     19\u001b[0m next_dog_pix = [os.path.join(train_dogs_dir, fname) \n\u001b[1;32m     20\u001b[0m                 for fname in os.listdir(train_dogs_dir)[pic_index-8:pic_index]]\n",
            "\u001b[0;31mNameError\u001b[0m: name 'train_cats_dir' is not defined"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1152x1152 with 0 Axes>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IvaNCN1ICqPK"
      },
      "source": [
        "import cv2\n",
        "import numpy as np\n",
        "\n",
        "# Gather data train\n",
        "train_data = []\n",
        "train_label = []\n",
        "for r, d, f in os.walk(train_dir):\n",
        "    for file in f:\n",
        "        if \".jpg\" in file:\n",
        "            imagePath = os.path.join(r, file)\n",
        "            image = cv2.imread(imagePath)\n",
        "            image = cv2.resize(image, (150,150))\n",
        "            train_data.append(image)\n",
        "            label = imagePath.split(os.path.sep)[-2]\n",
        "            train_label.append(label)\n",
        "\n",
        "train_data = np.array(train_data)\n",
        "train_label = np.array(train_label)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xytwR-S4Crro"
      },
      "source": [
        "# Gather data validation\n",
        "val_data = []\n",
        "val_label = []\n",
        "for r, d, f in os.walk(validation_dir):\n",
        "    for file in f:\n",
        "        if \".jpg\" in file:\n",
        "            imagePath = os.path.join(r, file)\n",
        "            image = cv2.imread(imagePath)\n",
        "            image = cv2.resize(image, (150,150))\n",
        "            val_data.append(image)\n",
        "            label = imagePath.split(os.path.sep)[-2]\n",
        "            val_label.append(label)\n",
        "\n",
        "val_data = np.array(val_data)\n",
        "val_label = np.array(val_label)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZRI9ZP2UCvGD"
      },
      "source": [
        "<h3>Data Preprocessing</h3>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kCEZIMVnCsFK",
        "outputId": "fa287df2-1d20-4242-d0e0-dc560d699369"
      },
      "source": [
        "# Tampilkan shape dari data train dan data validation\n",
        "print(\"Train Data = \", train_data.shape)\n",
        "print(\"Train Label = \", train_label.shape)\n",
        "print(\"Validation Data = \", val_data.shape)\n",
        "print(\"Validation Label = \", val_label.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Train Data =  (41, 150, 150, 3)\n",
            "Train Label =  (41,)\n",
            "Validation Data =  (41, 150, 150, 3)\n",
            "Validation Label =  (41,)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xxbZge_GCxtE",
        "outputId": "4995986b-2804-4a02-fce5-9d2938324780"
      },
      "source": [
        "# Normalisasi dataset\n",
        "print(\"Data sebelum di-normalisasi \", train_data[0][0][0])\n",
        "\n",
        "x_train = train_data.astype('float32') / 255.0\n",
        "x_val = val_data.astype('float32') / 255.0\n",
        "print(\"Data setelah di-normalisasi \", x_train[0][0][0])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Data sebelum di-normalisasi  [80 72 68]\n",
            "Data setelah di-normalisasi  [0.3137255  0.28235295 0.26666668]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TVP7wbecC1AO",
        "outputId": "ac576465-16df-4973-849c-374883ebebe9"
      },
      "source": [
        "# Transformasi label encoder\n",
        "from sklearn.preprocessing import LabelEncoder\n",
        "\n",
        "print(\"Label sebelum di-encoder \", train_label[995:1005])\n",
        "\n",
        "lb = LabelEncoder()\n",
        "y_train = lb.fit_transform(train_label)\n",
        "y_val = lb.fit_transform(val_label)\n",
        "\n",
        "print(\"Label setelah di-encoder \", y_train[995:1005])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Label sebelum di-encoder  []\n",
            "Label setelah di-encoder  []\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YLD6FXIKC35_"
      },
      "source": [
        "<h3>Definisikan Model</h3>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-IpFwrdNC5Sx"
      },
      "source": [
        "from tensorflow.keras import layers\n",
        "from tensorflow.keras import Model"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ukf5Oh1cC7QH"
      },
      "source": [
        "# Buat model dengan 1 input layer, 1 hidden layer, dan 1 output layer\n",
        "img_input = layers.Input(shape=(150, 150, 3)) # layer input\n",
        "x = layers.Flatten()(img_input) # ubah dari matriks 150x150x3 menjadi vektor\n",
        "x = layers.Dense(128, activation='relu')(x) # hidden layer 1 dengan 128 neuron\n",
        "output = layers.Dense(1, activation='sigmoid')(x) # output layer dengan 1 neuron (binary)\n",
        "\n",
        "# Definisikan modelnya\n",
        "model = Model(img_input, output)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hWPPCl28C8iJ",
        "outputId": "4707e755-1cce-4b3d-9356-16c5afc14292"
      },
      "source": [
        "# Tampilkan model summary\n",
        "model.summary()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"model\"\n",
            "_________________________________________________________________\n",
            " Layer (type)                Output Shape              Param #   \n",
            "=================================================================\n",
            " input_1 (InputLayer)        [(None, 150, 150, 3)]     0         \n",
            "                                                                 \n",
            " flatten (Flatten)           (None, 67500)             0         \n",
            "                                                                 \n",
            " dense (Dense)               (None, 128)               8640128   \n",
            "                                                                 \n",
            " dense_1 (Dense)             (None, 1)                 129       \n",
            "                                                                 \n",
            "=================================================================\n",
            "Total params: 8,640,257\n",
            "Trainable params: 8,640,257\n",
            "Non-trainable params: 0\n",
            "_________________________________________________________________\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TD_IAMQnC_ih",
        "outputId": "9266b116-4ddb-4c02-9c84-a08af9d7e2dd"
      },
      "source": [
        "from tensorflow.keras.optimizers import Adam\n",
        "\n",
        "# Compile model\n",
        "model.compile(loss='binary_crossentropy',\n",
        "              optimizer=Adam(lr=0.001),\n",
        "              metrics=['acc'])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/keras/optimizer_v2/adam.py:105: UserWarning: The `lr` argument is deprecated, use `learning_rate` instead.\n",
            "  super(Adam, self).__init__(name, **kwargs)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_BTSpUVlDAH0",
        "outputId": "10086cdd-63bd-4392-c7cd-51be035451b7"
      },
      "source": [
        "H = model.fit(x_train, y_train, batch_size=20, epochs=50, validation_data=(x_val, y_val))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/50\n",
            "3/3 [==============================] - 1s 150ms/step - loss: 27.1796 - acc: 0.4390 - val_loss: 3.1947 - val_acc: 0.5122\n",
            "Epoch 2/50\n",
            "3/3 [==============================] - 0s 71ms/step - loss: 2.5561 - acc: 0.4634 - val_loss: 11.7792 - val_acc: 0.5122\n",
            "Epoch 3/50\n",
            "3/3 [==============================] - 0s 70ms/step - loss: 7.9600 - acc: 0.6098 - val_loss: 18.4528 - val_acc: 0.5122\n",
            "Epoch 4/50\n",
            "3/3 [==============================] - 0s 71ms/step - loss: 18.6176 - acc: 0.5122 - val_loss: 9.5616 - val_acc: 0.5122\n",
            "Epoch 5/50\n",
            "3/3 [==============================] - 0s 71ms/step - loss: 16.4749 - acc: 0.5122 - val_loss: 20.6623 - val_acc: 0.5122\n",
            "Epoch 6/50\n",
            "3/3 [==============================] - 0s 69ms/step - loss: 15.8111 - acc: 0.5122 - val_loss: 4.2334 - val_acc: 0.6098\n",
            "Epoch 7/50\n",
            "3/3 [==============================] - 0s 71ms/step - loss: 6.6622 - acc: 0.5854 - val_loss: 0.1478 - val_acc: 0.9512\n",
            "Epoch 8/50\n",
            "3/3 [==============================] - 0s 70ms/step - loss: 3.1275 - acc: 0.7317 - val_loss: 14.8520 - val_acc: 0.5122\n",
            "Epoch 9/50\n",
            "3/3 [==============================] - 0s 71ms/step - loss: 12.6894 - acc: 0.5366 - val_loss: 0.0773 - val_acc: 0.9512\n",
            "Epoch 10/50\n",
            "3/3 [==============================] - 0s 76ms/step - loss: 0.5283 - acc: 0.9268 - val_loss: 0.5402 - val_acc: 0.9512\n",
            "Epoch 11/50\n",
            "3/3 [==============================] - 0s 73ms/step - loss: 0.0463 - acc: 0.9756 - val_loss: 6.9944 - val_acc: 0.6341\n",
            "Epoch 12/50\n",
            "3/3 [==============================] - 0s 80ms/step - loss: 8.2717 - acc: 0.6098 - val_loss: 0.2662 - val_acc: 0.9512\n",
            "Epoch 13/50\n",
            "3/3 [==============================] - 0s 69ms/step - loss: 2.8973 - acc: 0.8537 - val_loss: 16.3897 - val_acc: 0.5854\n",
            "Epoch 14/50\n",
            "3/3 [==============================] - 0s 70ms/step - loss: 17.6613 - acc: 0.5854 - val_loss: 8.4575 - val_acc: 0.6829\n",
            "Epoch 15/50\n",
            "3/3 [==============================] - 0s 72ms/step - loss: 6.0162 - acc: 0.7317 - val_loss: 0.2162 - val_acc: 0.9756\n",
            "Epoch 16/50\n",
            "3/3 [==============================] - 0s 72ms/step - loss: 1.9597 - acc: 0.8780 - val_loss: 9.6700 - val_acc: 0.5854\n",
            "Epoch 17/50\n",
            "3/3 [==============================] - 0s 79ms/step - loss: 8.1109 - acc: 0.6098 - val_loss: 0.2529 - val_acc: 0.9512\n",
            "Epoch 18/50\n",
            "3/3 [==============================] - 0s 70ms/step - loss: 0.3214 - acc: 0.9512 - val_loss: 0.9516 - val_acc: 0.9512\n",
            "Epoch 19/50\n",
            "3/3 [==============================] - 0s 71ms/step - loss: 1.4841 - acc: 0.9268 - val_loss: 2.4808 - val_acc: 0.8537\n",
            "Epoch 20/50\n",
            "3/3 [==============================] - 0s 73ms/step - loss: 2.3168 - acc: 0.8537 - val_loss: 0.9450 - val_acc: 0.9512\n",
            "Epoch 21/50\n",
            "3/3 [==============================] - 0s 72ms/step - loss: 0.7952 - acc: 0.9512 - val_loss: 0.0750 - val_acc: 0.9756\n",
            "Epoch 22/50\n",
            "3/3 [==============================] - 0s 69ms/step - loss: 0.1853 - acc: 0.9512 - val_loss: 0.3599 - val_acc: 0.9756\n",
            "Epoch 23/50\n",
            "3/3 [==============================] - 0s 73ms/step - loss: 0.4062 - acc: 0.9512 - val_loss: 0.5613 - val_acc: 0.9268\n",
            "Epoch 24/50\n",
            "3/3 [==============================] - 0s 70ms/step - loss: 0.5086 - acc: 0.9268 - val_loss: 0.2504 - val_acc: 0.9756\n",
            "Epoch 25/50\n",
            "3/3 [==============================] - 0s 70ms/step - loss: 0.2503 - acc: 0.9756 - val_loss: 0.0730 - val_acc: 0.9756\n",
            "Epoch 26/50\n",
            "3/3 [==============================] - 0s 70ms/step - loss: 0.1578 - acc: 0.9756 - val_loss: 0.2235 - val_acc: 0.9756\n",
            "Epoch 27/50\n",
            "3/3 [==============================] - 0s 69ms/step - loss: 0.2518 - acc: 0.9756 - val_loss: 0.2137 - val_acc: 0.9756\n",
            "Epoch 28/50\n",
            "3/3 [==============================] - 0s 73ms/step - loss: 0.2137 - acc: 0.9756 - val_loss: 0.0509 - val_acc: 0.9756\n",
            "Epoch 29/50\n",
            "3/3 [==============================] - 0s 72ms/step - loss: 0.0943 - acc: 0.9512 - val_loss: 0.1160 - val_acc: 0.9756\n",
            "Epoch 30/50\n",
            "3/3 [==============================] - 0s 69ms/step - loss: 0.1160 - acc: 0.9756 - val_loss: 0.0745 - val_acc: 0.9756\n",
            "Epoch 31/50\n",
            "3/3 [==============================] - 0s 70ms/step - loss: 0.0656 - acc: 0.9756 - val_loss: 0.0489 - val_acc: 0.9756\n",
            "Epoch 32/50\n",
            "3/3 [==============================] - 0s 69ms/step - loss: 0.0485 - acc: 0.9756 - val_loss: 0.0653 - val_acc: 0.9756\n",
            "Epoch 33/50\n",
            "3/3 [==============================] - 0s 76ms/step - loss: 0.0653 - acc: 0.9756 - val_loss: 0.0445 - val_acc: 0.9756\n",
            "Epoch 34/50\n",
            "3/3 [==============================] - 0s 73ms/step - loss: 0.0445 - acc: 0.9756 - val_loss: 0.0382 - val_acc: 0.9756\n",
            "Epoch 35/50\n",
            "3/3 [==============================] - 0s 68ms/step - loss: 0.0577 - acc: 0.9512 - val_loss: 0.0376 - val_acc: 0.9756\n",
            "Epoch 36/50\n",
            "3/3 [==============================] - 0s 70ms/step - loss: 0.0502 - acc: 0.9756 - val_loss: 0.0369 - val_acc: 0.9756\n",
            "Epoch 37/50\n",
            "3/3 [==============================] - 0s 71ms/step - loss: 0.0419 - acc: 0.9756 - val_loss: 0.0418 - val_acc: 0.9756\n",
            "Epoch 38/50\n",
            "3/3 [==============================] - 0s 74ms/step - loss: 0.0418 - acc: 0.9756 - val_loss: 0.0383 - val_acc: 0.9756\n",
            "Epoch 39/50\n",
            "3/3 [==============================] - 0s 69ms/step - loss: 0.0624 - acc: 0.9756 - val_loss: 0.0346 - val_acc: 0.9756\n",
            "Epoch 40/50\n",
            "3/3 [==============================] - 0s 70ms/step - loss: 0.0678 - acc: 0.9512 - val_loss: 0.0482 - val_acc: 0.9756\n",
            "Epoch 41/50\n",
            "3/3 [==============================] - 0s 77ms/step - loss: 0.0990 - acc: 0.9512 - val_loss: 1.0950 - val_acc: 0.9268\n",
            "Epoch 42/50\n",
            "3/3 [==============================] - 0s 71ms/step - loss: 2.3252 - acc: 0.8293 - val_loss: 12.8391 - val_acc: 0.5366\n",
            "Epoch 43/50\n",
            "3/3 [==============================] - 0s 71ms/step - loss: 9.3561 - acc: 0.6098 - val_loss: 1.3876 - val_acc: 0.9756\n",
            "Epoch 44/50\n",
            "3/3 [==============================] - 0s 69ms/step - loss: 1.6026 - acc: 0.9268 - val_loss: 6.9872 - val_acc: 0.7073\n",
            "Epoch 45/50\n",
            "3/3 [==============================] - 0s 73ms/step - loss: 7.3055 - acc: 0.6829 - val_loss: 2.6121 - val_acc: 0.8780\n",
            "Epoch 46/50\n",
            "3/3 [==============================] - 0s 71ms/step - loss: 2.0136 - acc: 0.8780 - val_loss: 2.0274 - val_acc: 0.9756\n",
            "Epoch 47/50\n",
            "3/3 [==============================] - 0s 72ms/step - loss: 2.0274 - acc: 0.9756 - val_loss: 3.1501 - val_acc: 0.8780\n",
            "Epoch 48/50\n",
            "3/3 [==============================] - 0s 72ms/step - loss: 3.5937 - acc: 0.8537 - val_loss: 1.5476 - val_acc: 0.9756\n",
            "Epoch 49/50\n",
            "3/3 [==============================] - 0s 77ms/step - loss: 2.3993 - acc: 0.9512 - val_loss: 42.4505 - val_acc: 0.5122\n",
            "Epoch 50/50\n",
            "3/3 [==============================] - 0s 70ms/step - loss: 45.5013 - acc: 0.5122 - val_loss: 39.3801 - val_acc: 0.5122\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FEWlFuCbDFEV"
      },
      "source": [
        "<h3>Evaluasi Model</h3>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 299
        },
        "id": "fLJK8najDB8a",
        "outputId": "33d87897-6b4e-4e9c-a92d-c5e0d3e38fdd"
      },
      "source": [
        "plt.style.use(\"ggplot\")\n",
        "plt.figure()\n",
        "plt.plot(np.arange(0, 50), H.history[\"loss\"], label=\"train_loss\")\n",
        "plt.plot(np.arange(0, 50), H.history[\"val_loss\"], label=\"val_loss\")\n",
        "plt.title(\"Loss Plot\")\n",
        "plt.xlabel(\"Epoch #\")\n",
        "plt.ylabel(\"Loss\")\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYEAAAEaCAYAAAD3+OukAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOydeZRcZZn/P7f26q16705v6WwEsgCyB2QRwibLoI6DMsEDwvxwnBk0zuggOkQdWRQxkRl01NFBAQ/OAIMsRiUgAWTQABIg+55OOr1XV69Vt6ru+/vj1q2utbvTqerudD+fc3I6fetW1ft2V9/nPutXU0opBEEQhFmJbaoXIAiCIEwdYgQEQRBmMWIEBEEQZjFiBARBEGYxYgQEQRBmMWIEBEEQZjFiBARhGnDRRRdx6623TvUyhFmIGAFhxnHTTTexcuXKqV5GnIcffhhN0+L/ampquPrqq3nvvfeO6XUdDgcPP/xwbhYpzFrECAjCJGC32zly5AhHjhzh6aefpqOjg8svv5xAIDDVSxNmOWIEhFnHjh07uOqqqygqKqKoqIhrrrmG3bt3xx/v6+vj5ptvpra2FrfbTWNjI1/4whfij7/22mucd955FBcXU1xczCmnnMJvf/vbMd+3traW2tpaVqxYwdq1azly5AhvvPFGxnPD4TB33HEH9fX1uFwulixZwi9+8Yv4483NzUSjUW6++ea4hyEIE0GMgDCrGB4e5rLLLiMYDLJx40Y2btzIwMAAV1xxBbquA/DVr36Vt99+m1/96lfs2rWLX/7yl5x00kkARCIRrr32Ws4++2zefvtt3n77bb72ta9RUFBwVOvwer2AebHPxJ133smPf/xj1q1bx/vvv8+qVatYtWoVL774IgCbNm3Cbrezbt26uIchCBPBMdULEITJ5Be/+AWdnZ289dZbVFZWAvD444/T3NzM448/zqc+9SkOHDjABz7wAc4++2wAmpqaOPfccwHo7+/H7/dz7bXXsmjRIoD41/HS2dnJmjVrKCkp4ayzzkp7fGhoiAcffJC1a9fy8Y9/HDCNwqZNm7j77ru55JJLqKqqAsDn81FbWzuxH4YgIJ6AMMvYsmULS5YsiRsAgJqaGhYvXsyWLVsA+OxnP8sTTzzBsmXL+NznPsf69esxDAOAsrIybr31Vi6//HKuvPJK7rvvPnbs2DHm+0aj0Xj4qbq6mt27d/PEE09QXV2ddu7u3bvRdZ0LLrgg6fiFF14YX6Mg5AoxAoKQwuWXX87Bgwf5yle+QjAYZNWqVVx88cVEo1EAfvzjH/PWW29x6aWXsnHjRpYtW8YPf/jDUV/TbrfzzjvvsHnzZvr6+ti2bRuXXnrpZGxHEEZFjIAwq1i6dClbt26lq6srfqy9vZ0dO3awbNmy+LHy8nI++clP8sMf/pDnn3+ejRs3snXr1vjjy5Yt4wtf+ALr16/nlltu4Uc/+tGY771w4UIWLFhAcXHxmOe53W5eeeWVpOOWwbFwuVxxwyQIE0VyAsKMZGBggHfeeSfpmMfj4YYbbuAb3/gG119/Pffffz9KKf7pn/6J+vp6rr/+egC+8pWvcPrpp7N06VJsNhuPPfYYRUVFNDU1sXv3bn784x9zzTXX0NjYSGtrK6+++iqnnXZaztZeUFDA7bffzr/8y79QVVXFKaecwhNPPMGvfvUrXnjhhfh58+bN4/e//z1XXnklLpcrKcQlCONFjIAwI/njH//IBz7wgaRjixcvZvv27fzud79j9erV8Zj7RRddxG9+8xtcLhdgGou77rqL/fv3Y7fbOfXUU1m/fj0+n4+hoSF27drFJz7xCTo7O6moqOCqq67iO9/5Tk7Xf/fdd2Oz2fj85z9PZ2cnCxcu5NFHH+WSSy6Jn/PAAw+wevVqmpubCYfDiD6UMBE0URYTBEGYvUhOQBAEYRYjRkAQBGEWI0ZAEARhFiNGQBAEYRYjRkAQBGEWc1yWiLa2tk7oeZWVlUlNQrMF2ffsYrbuG2bv3sez77q6uozHxRMQBEGYxYgREARBmMWIERAEQZjFHJc5gVSUUgSDQQzDGFVhqb29nVAoNIkrmx6Md99KKWw2Gx6PR5SqBGGWMCOMQDAYxOl04nCMvh2Hw4Hdbp+kVU0fjmbfkUiEYDAYV74SBGFmMyPCQYZhjGkAhPHhcDjiAiqCIMx8ZoQRkNBFbpGfpyDMHmaEERAEQZjJqEP7MX71GKqvN+evLUZAEARhmqMOH0A990sYHsr5a4sRyAGBQICHH374qJ934403EggEjvp5n//853nuueeO+nmCIByn6LHqPqcz5y8tRiAH9PX18fOf/zzteCQSGfV5jzzyCD6fL1/LEgRhphAJm1+d7py/9IwrqTEe/zGqZV/mxzRtQhJ8WuM8bJ/4m6yP33PPPRw4cIBLL70Up9OJ2+3G5/Oxe/duXnvtNT796U/T2tpKKBTilltuYdWqVQCcffbZrF+/nsHBQVatWsVZZ53Fm2++SW1tLT/96U/HVab56quv8q//+q9Eo1FOOeUU7r33XtxuN/fccw+/+93vcDgcXHTRRXz1q1/l2WefZe3atdhsNkpKSnjqqaeO+mchCMIUoOvm1zx4AjPOCEwFd955Jzt27OCFF17g9ddf51Of+hQvvfQSTU1NgKkFW1ZWxvDwMFdddRUf/vCHKS8vT3qNffv28dBDD3H//fdz22238etf/5qPfexjo75vMBhk9erV/PKXv2TBggXcfvvt/PznP+djH/sY69ev55VXXkHTNAYHBwFYt24djz32GHPmzJlQGEoQhCkibBkBV85fesYZgdHu2B0Ox5ghmlxw6qmnxg0AwE9/+lPWr18PmBNQ9+3bl2YEGhsbWbZsGQAnn3wyLS0tY77Pnj17aGpqYsGCBQB8/OMf52c/+xk333wzbrebf/zHf2TlypVcccUVAJxxxhmsXr2aa665hiuvvDInexUEYRII62C3o+Wh2VVyAnmgoKAg/v/XX3+dV199lWeffZYNGzawbNmyjCMc3O6RWJ/dbicajU74/R0OB88//zxXXXUVGzZs4BOf+AQA3/rWt/jSl75Ea2srV155JT09PRN+D0EQJpGwDo7cewEwAz2BqaCwsJCBgYGMj/X39+Pz+fB6vezevZu33347Z++7YMECWlpa2LdvH/PmzePJJ5/knHPOYXBwkOHhYS655BLOPPNMzj33XAD279/Paaedxmmnncbvf/97Wltb0zwSQRCmIWEdXGIEpi3l5eWceeaZXHzxxXg8HiorK+OPXXTRRTzyyCNceOGFLFiwgNNOOy1n7+vxePjud7/LbbfdFk8M33jjjfT29vLpT3+aUCiEUoqvf/3rAHzzm99k3759KKX44Ac/yNKlS3O2FkEQ8khYz0tSGEBTEymXmWJSlcWGhoaSQjDZmKycwHTjaPc93p/ndEdUpmYfM3Xvxo/uRx3ci/2bP8j4uCiLCYIgzGBUOJw3T0DCQdOYO++8k02bNiUdu/XWW7n++uunaEWCIEwJ4VBeykNBjMC05p577pnqJQiCMImEIgaDYYNyb8qlORzOmxGQcJAgCMI04amt3fz9s3vpD6WUiOexOkiMgCAIwjTBPxxlMGywfqc/+YE89gmIERAEQZgm6FFT1e+5HX5CkQSFP11HE09AEARhZqNHFQ6bRiAU5cW9CfO9IvnrExAjMAUsWrQo62MtLS1cfPHFk7gaQRCmC3rUoNHnYnGlh6e39RA1Ym1cup6XMdIgRkAQBGHaEIoqXHYbH11SQftAmD8c7DcfkD6B8fOfb7azzx/M+Jg2QT2BeWUebj2jJuvj99xzD3V1ddx0002AOTrabrfz+uuvEwgEiEQifOlLX+Lyyy8/qvcNBoN8+ctf5t1338Vut7NmzRrOO+88duzYwRe+8AV0XUcpxY9+9CNqa2u57bbbOHLkCIZh8LnPfY6/+Iu/OOq9CoIwdegRhduucVZDEQ0lLp7a2s35c4tjfQL58QRmnBGYCq699lrWrFkTNwLPPvssjz32GLfccgvFxcX09PRwzTXXcNlll6Fp2rhf9+GHH0bTNF588UV2797NJz/5SV599VUeeeQRbrnlFj760Y+i6zrRaJSXXnqJ2tpaHnnkEcBUOxME4fhCjxoUuRzYNI2PLCnn395o48+H+znFMGaGJ2AYBnfccQfl5eXccccddHR0sG7dOvr7+5k/fz7/8A//gMNxbEsa7Y49X7ODli1bRldXF21tbXR3d+Pz+aiuruZrX/saf/zjH9E0jba2Njo7O6murh73627atImbb74ZgIULF9LQ0MDevXs5/fTTefDBBzly5AhXXnkl8+fP58QTT+Qb3/gGd999NytXruTss8/O+T4FQcgvelThcphR+gubS/jF5i6e2trNKTAz+gR+/etfU19fH//+0Ucf5aqrruLf/u3fKCws5KWXXprM5eSUq6++mueff55nnnmGa6+9lqeeeoru7m7Wr1/PCy+8QGVlZUYdgYnwkY98hP/6r//C4/Fw44038tprr7FgwQJ+85vfcOKJJ/Ltb3+btWvX5uS9BEGYPPSogctuRgucdhvXnlTGe50hdhU3HP8dw93d3bz99ttccsklACil2LJlC+eccw5gjlxOnZNzPHHttdfyq1/9iueff56rr76a/v5+KisrcTqd/OEPf+DQoUNH/ZpnnXUW//u//wuYKmKHDx9mwYIFHDhwgLlz53LLLbdw+eWXs23bNtra2vB6vXzsYx/jM5/5DO+9916utygIQp4JRRVu+8hl+bKFpRQ6NP636aLjf3bQww8/zKpVqxgeHgZMsZWCggLsMbm08vLyrEpXGzZsYMOGDQDcd999SfP6Adrb28cdRjrWcFM2li5dyuDgIHPmzKG+vp6Pf/zj3HjjjVxyySWceuqpLFq0CLvdHn//bOuwfh4Oh4NbbrmFf/7nf+aSSy7B4XDw4IMPUlhYyPPPP88TTzyBw+Ggurqa1atX88477/D1r38dm82G0+nkW9/6VtJ7HM2+3W532s/4eMThcMyIfRwts3XfcPzvPWLsoqSoIGkPH1nYzmPhZQQKQizKsrdj2fekGIG33noLn8/H/Pnz2bJly1E/f+XKlaxcuTL+ferc7FAoFL94jka+9QRefPFFACKRCD6fj2eeeSbtnEgkwq5du7Kuo66ujpdeeolIJILD4eCBBx5Ie/5nP/tZPvvZzyYdP//88+OGMvFcOPp9h0KhGTGTfabOlh+L2bpvOP73HopEMfRg0h5Wlgb5pYry2BEbf59lb8eiJzApRmDHjh28+eab/PnPf0bXdYaHh3n44YcZGhoiGo1it9vp6ekRqUNBEGYtUUMRMYgnhi1KtTAXH3mTF+3ncMNwJH3C6DEyKUbghhtu4IYbbgBgy5YtPPvss9x+++1897vf5Y033uC8887j5Zdf5owzzpiM5UwLtm3bxu233550zO1289xzz03RigRBmEr0qNnDZCWG44R1/qJlI8HlZ490EOeQKe0T+Ou//mvWrVvH448/zrx58yY8LuE4VMjkpJNO4oUXXpjqZWTkePx5CsLxjjU8LjExDEBYpzbYw+oTbGiFue8VmHQjsHTp0rjAeU1NDffee+8xv6bNZovH0IVjIxKJYLPJNBFBmGyyegK6bn51ScdwVjweD8FgkFAoNGpHrtvtzlmt/vHEePetlMJms+HxeCZhVYIgJBKKeQKpRkCFY0ZgJnQM5wtN0/B6vWOed7xXDkyU2bpvQTie0CMxT8CRHg4CZIqoIAjCTMYKB7nTEsNh86voCQiCIMxc9Hg4KNUTiIVyZ8LsIEEQBCEz2UtEY56AaAwLgiDMXLIlhtF10GwwjqkIE0GMgCAIwjQgnhhODQdFdHC5jkqL5GgQIyAIgjANiIeDHBk8gTwlhUGMgCAIwrQge2I4fyLzIEZAEARhWhDKWiIqnoAgCMKMx/IEnJk6hvMkKANiBARBEKYF4ajCadOwpSaAxQgIgiDMfEJRlZ4UBrNPIE+NYiBGQBAEYVqgR4z0pDCAHspboxiIERAEQZgW6FGVnhQG8QQEQRBmA3rUSO8WBojoaJITEARBmNnoUZUlHCSJYUEQhBlPKKoyewLSJyAIgjDz0SNGuqAMSMewIAjCbGDUxLB4AoIgCDObTIlhZUQhGpHqIEEQhJlOKFNiOC4tKUZAEARhRqNnSgzrlsi8GAFBEIQZjdkxnGFuEIgREARBmMkopTL3CYgREARBmPlEDIUig6pYzAhIx7AgCMIMZkRQJosnINVBgiAIM5ewpS+cLSfgkD4BQRCEGcuIvnCW6iCXdAwLgiDMWEJxTyDlkhyxEsPiCQiCIMxY9EjMCKQkhlW8T0A8AUEQhBmLFQ5KTwxbHcPiCQiCIMxY9KyJ4ZD5VaqDBEEQZi6heGI4iyeQR41hR95eOQFd11mzZg2RSIRoNMo555zDX/3VX9HR0cG6devo7+9n/vz5/MM//AMOx6QsSRAEYdqQLSeAHvME8tgsNilXXKfTyZo1a/B4PEQiEe666y5OPfVUnnvuOa666irOO+88fvSjH/HSSy9x2WWXTcaSBEEQpg0jOYEUIxAJg6ZBHm+OJyUcpGkaHo8HgGg0SjQaRdM0tmzZwjnnnAPARRddxKZNmyZjOYIgCNMKPVuJqG5KS2paBrGZHDFpsRfDMPjnf/5n2trauPzyy6mpqaGgoAC73Q5AeXk5PT09k7UcQRCEaUP2xHB+pSVhEo2AzWbj/vvvZ3BwkO985zu0traO+7kbNmxgw4YNANx3331UVlZOaA0Oh2PCzz2ekX3PLmbrvuH43bvDPQxAXU0VzgRvIGC3obvdY+7pWPY96VnYwsJCli5dys6dOxkaGiIajWK32+np6aG8vDzjc1auXMnKlSvj33d1dU3ovSsrKyf83OMZ2ffsYrbuG47fvfv7BtCA3p7upNCP0d+HsjvG3NN49l1XV5fx+KTkBPr6+hgcHATMSqF3332X+vp6li5dyhtvvAHAyy+/zBlnnDEZyxEEQZhWWPrCqbF/FdbzWhkEk+QJ+P1+HnroIQzDQCnFihUrOP3002loaGDdunU8/vjjzJs3j4svvngyliMIgjCt0KMKlyPDPXk4PDOMwNy5c/n2t7+ddrympoZ77713MpYgCIIwbQll0hcGs08gz0ZAOoYFQRCmGD1qpPcIgNknkMeRESBGQBAEYcoJZ9IXBvEEBEEQZgNZw0HhcF71hUGMgCAIwpSjR4wsiWE9r2OkQYyAIAjClKNHVeacwCR0DIsREARBmGKsPoE0JsETmDVzm42f/zu9eghu/cepXoogCEISerbEcFjPe3XQrDECaqCPSFf7VC9DEAQhjUyJYWVEIRLJq6AMzKJwkOYtRA0NTvUyBEEQ0tCjGRLD4Yj5VfoEcoS3ADU0MNWrEARBSEOPZEgMh/OvKgazyggUooaHTBdLEARhmmAoRdjI0Cdg6QuLEcgR3gLza3B4atchCIKQQDibqph4AjnGMgLDQ1O7DkEQhARCWVXFTE9Ak5xAbtAKCs3/DEtyWBCE6YMlMp9RXxikOihneGKewJB4AoIgTB/0yCj6wiDVQTkjnhMQIyAIwvQh7gk4UoxAJGYEZHZQjvCa4SAlOQFBEKYRVk7AnS0clOfZQePuGH7//feprq6muroav9/PY489hs1m44YbbqC0tDSfa8wN8cSw5AQEQZg+hLMkhlW8RHSaeAI/+clPsNnM03/+858TjUbRNI0f/vCHeVtcTvFaiWHxBARBmD5kTQxPUonouD2Bnp4eKisriUajbN68me9///s4HA5uu+22fK4vd7hcYLeLJyAIwrRirBLRaWMEvF4vvb29tLS00NDQgMfjIRKJEIlE8rm+nKFpGlpBkXgCgiBMK/RIlsTwdPMErrjiCr785S8TiUS46aabANi+fTv19fX5WlvOsRUUYogREARhGqFnSwxbnsB0GSV93XXXcdZZZ2Gz2aitrQWgvLycz3zmM3lbXK7RCgqlOkgQhGmFni0cFG8Wm0aiMnV1dfH/v//++9hsNpYsWZLzReULMxwkOQFBEKYPoayJYR2cLjQtg+JYDhl3ddCaNWvYvn07AE8//TTf+973+N73vsdTTz2Vt8XlGltBoeQEBEGYVmT1BCZBWhKOwgi0tLRwwgknAPDiiy+yZs0a7r77bl544YW8LS7XaIWSGBYEYXqhRwwcNrDbMhmB/DaKwVGEg5QyrVVbWxsADQ0NAAwOHj/hFQkHCYIw3RhVX3gSPIFxG4HFixfz05/+FL/fz5lnngmYBqG4uDhvi8s1ZjhoGKVU3uNsgiAI40HPoC8MoGI5gXwz7nDQ3/3d31FQUMDcuXP5q7/6KwBaW1v58Ic/nLfF5RqtoAiUAaHgVC9FEAQBMBPDGT0BfXKMwLg9geLiYm644YakY6eddlrOF5RPRjQFhsDjndrFCIIgkN0TIBLOe48AHIURiEQiPPXUU7zyyiv4/X7Kysq44IIL+OhHP4rDcVSVplOGLVFYpqxiahcjCIKAmRjOaAT0ELimUWL40UcfZc+ePfzN3/wNVVVVdHZ28uSTTzI0NBTvIJ7uaAVF5n+kQkgQhGlC9sRwGArzn3MdtxF44403uP/+++OJ4Lq6OubNm8cXv/jF48cIFFpGQCqEBEGYHoSiCnfq3CCYfn0CVono8YwVDpLREYIgTBfCUQN3pnBQWEebTn0CK1as4Fvf+hZ/+Zd/SWVlJV1dXTz55JOsWLEin+vLKSPhoPx4ApvbBinzOGgqzf8vThCEmcFx0yewatUqnnzySX7yk5/g9/spLy/n3HPPHdco6a6uLh566CF6e3vRNI2VK1fy4Q9/mIGBAdauXUtnZydVVVWsXr2aoqKiY9rQaGiFVmJ4OC+vv/b1Iyyp8vKl84+fyaqCIEwtejRLYjisT6/EsMPh4Prrr+f666+PH9N1nRtvvJFVq1aN+ly73c6NN97I/PnzGR4e5o477uDkk0/m5ZdfZvny5Vx33XU8/fTTPP3002O+1rGgub2gaXnxBEIRA/9whEDw+NBXEARhehDK5gnoet4niMIxCs2Pt+u2rKyM+fPnA6Y4TX19PT09PWzatIkLL7wQgAsvvJBNmzYdy3LGRLPZwFOQl+qg9kFz9ndvMJrz1xYEYeaiR1SaoIxSavr1CeSKjo4O9u3bx8KFCwkEApSVlQFQWlpKIBDI+JwNGzawYcMGAO677z4qKysn9N4OhwNbUREuI4pvgq+RjZ39PQD06caE15cvHA7HtFvTZCD7nn0cj3vXjR2UFhUmrVuFQnQAhb5SCsexn2PZ95hG4P3338/62NFKSwaDQR544AFuuukmCgoKkh7TNC2rZ7Fy5UpWrlwZ/76rq+uo3teisrISw+Uh2NtDeIKvkY1drX4A+oIR2jo6caROBJxCrET+bEP2Pfs43vYeNZT5Tw8mrVsNDgAwGI4wPI79jGffiXowiYxpBH7wgx+M+ebjIRKJ8MADD3D++edz9tlnA+Dz+eLdx36/n5KSknG91jHhzY+mQPuAHv9/XyhKuff46KIWBGHqGBGUmRp9YRiHEXjooYeO+U2UUvzHf/wH9fX1XH311fHjZ5xxBhs3buS6665j48aN8emkecVbAAF/zl/WygkA9A5HxAgIgjAmI4IyWfSFp4MRyAU7duzglVdeoampiS9+8YsAfPKTn+S6665j7dq1vPTSS/ES0XyjeQtRbYdy/rrtA2EKnTYGwwaBkCSHBUEYGz0SE5lP7Ri29IVnihE48cQT+e///u+Mj911112TsYQRvN5jCgcppVDP/xLtjPPRakf6AToGwyyq8PBO25CUiQqCMC70bPrCEdMIaJNQHXRMJaLHJbGcwFhjMI706/zj+v34h1Mu6F3tqF/9AuOH30bFEuMDepRB3eCESnM8dUDKRAVBGAdZ9YXjnsA07xM4LvEWQDRiduONwp8ODbC7J8jWjhSvodOU1+TQPtSv/weAjgEzfjevzI3DptErnoAgCOMge2LYMgL57xiehUYgQVhmFHZ2m6MlWvqSjYWyjMDi5ahf/zfq4F7aY0agpsiFz2OXhjFBEMaF5Qm40xLD4gnkD2+sP2GM0RE7u0wJykOBUPIDnW3gcGC77UtQWIzxX9+jrc88t6bQSanHMWNzAmrrOyh/91QvQxBmDFZi2CmewOShecceItcbjNARK/k8lOoJdLVBRQ1asQ/bjZ+FQ/to37qdQqeNIredUo99RuYElGFg/Ps3Ub99aqqXIggzBj1LOEhJTiCPjMMT2NllGogTKjwc7tOJGglJ5M42qKoFQDv1HLSzLqS9vZtql3mOGQ6agZ7AYD+E9ZFwmCAIx0zICgc5MlcHTcbsoFlsBLLnBHZ2BbFpcOG8EvSoinsFSinobEOrqomfq33yb+jwVlLdvgcVieBzOwgEozNChCeJgDkbie6OqV2HIMwgwmNWB4kRyD0xI6BG8QR2dQ/TXOpmQZkHgEOB2C9kaMA0HpW1IycXFtNRUEG1/xDq1/9DqddO2FAMR4y8bWFKCPSaX7s7Zp6BE4QpImufgNUx7BAjkHvGqA4ylGJXd5ATKr00+MykTEtfLDkcC4Vo1SNGoDcYRVcaNTUVqF//NyX95hCnmZYXUJYnEByGIdFoFoRcEMrmCcRnB0lOIPd4zYaubDmB1j6dwbDBogoPxbFEr+UJxOPhCZ5AvDz0/POhyEfJU/8JgP9gS542kF8GQlE+9/w+9vuDyQ8kzluSkJAg5IRsiWHCYXA4TA2UPDPrjIBms4Pbm7U6aGe3efGzun8bfG4OpXgCVI7kBKzpobWVPmxfeYCyD5wOgP/R/yT6va+hdrx3XIVPDgZC7O8N8WZripEUIyAIOUePKFz2DGP0w/qklIfCLDQCgJkXyOIJ7OwapsBpo6HEjMU1lrg4FNDNC3lXO5SUonm88fOt6aHVRU60sgpKr/kYAH1nXgIH9mB85ysY934RtXNLnjeVG6zKpgP+lP6I3h4oLAZAiREQhJwwqr7wJISCYBYbAZUlJ7CzO8jCCg+2mGVu8LkYDBv4g1FUx5F4eahF+0AYn8eOJ1biVeI2Z/IFFp2K7b7/RPvrvwV/N8ZP1+ZxQ7nDymXs700OB64KkecAACAASURBVKk+P9TPNUvWxAgIQk4YVV94EiqDYBYbgUyeQChisN8f5ISKkTv9hhLTJTsUCEFXO1pCKAjMuUE1hSMW22nXKHLZCAQjaC43touuRLvoSrOqJpi9QW26YHkCh/p0wtGECqeAH81XBhU14gkIQo7Qo2oUT0CMQP7wZhab3+sPElVmk5hFo8/8RbT4h6GnK90TGAxTU5TstpmjI0aqg7Q5DbGTW3O1g7xhzT0yFLQEErqlA37wlUNFFXR3TtHqBGFmoUeN9LlBgJokkXmYpUZAyyIxac0LspLCAOVeBwVOGy0dAVBGkhGIGorOwTA1Rcm/LJ/Hnjw/qNY0AkcjZnOkf/Qpp/kiEIzE70z295p5ARUcglAQSsvQKqolHCQIOUKPKFypgjIAekg8gbySJRy0s3uYqgIHZQnSkJqm0VDi4lAsRq4llId2DYUxFGmegM/jSJ4kWjUHbDYYpxHY5w/ymWf2sq0z91rIY9EbjLKowoPLrnEgZgTijWIlZVBRDYP9pmEQBOGYyJ4YDosRyCveQshwEbOaxFJp8Lk5NBQr86xK7xGoLkwxAu5kT0BzOs3egiPjMwKtsaF1rX2T7w30Bk195Eafe6RXINYopvnKoLzKPCYhIUE4ZrImhiUnkGe8BaDrcWUwMMMg7QOmRGQqjSUu/IaDQU8J+Mrix62ZQmk5Aa+Dft0gkjh4bk7DuMNBPTE1M/8UdB33DkfxeRw0l7pHwkFWj4CvfCQxLiEhQThmJDE8VWQYHZEpH2DREEsOH5qzOKmDr30gjE2DqgyeAEBfguC8VlsP7a0oY+wLuyVpmSZtmWdCEYPhiEGpx05zmZveYJTe4cjI8LjSMjMxDCjxBAThmMmWGCasmxGESWCWGoH0cdI7u4exabCwPIMnEJshdKiiOel4+0CYCq8Dhy3Zkpd6zJxC73BKcjgSHlcYxfIAJtsIWBVNpTFPAGLJ4V4/OBxQUGTmBRwO6G6f1LUJwkxEj6h0QRkwPQGXdAznDS3DOOmdXcPMLXWnz/UGqgocOI0wh4rnJB1vH0gvDwWzOgggkOQJxMpExxESmipPwOoR8HnsCUYgCH1+KClD0zTTEyqXMlFByAVZE8O6Dg7xBPJHiicQnxxakR4KArAP9VM31MkhZ2nS8Y7BMNVF6XE7yxNILhOtB0CNIzkcNwKTLE6T6AmUeByUex3s94fMnEBCLoSKamkYE4QcoEdVxhtPIrr0CeQVKycQqxBq7Tcnh55QmR4KAqCzjYahDg6pgvghPWrQMxwZ3RNIbBgrKoFi33HhCVhGLJ4cthrFYkivgCAcO0qpjIlhpZSMjcg7lrDMkGkE4knhLJ6A6myjYbCDjrCNUEwsJl4ZVJhuBAqcNhw2LV1msrZ+zAqhiKEIhKJ4HDaCEcVQePIqhBLDQQDNZW5aAjqRvl40X4IXVFENfb0oPZTpZQRhWvGHg33J+blpQsRQKDKMkbaqFsUI5JGU6qCdXcN4HTbqS7L80GOegAIOx2r3OwYyl4eC2WBW6rEnN4wRywu0HR51adaFeH6ZGZP3D4+8hjIMjP/4Fmrb5tH3N0ECwShehy3uns4tdRMxFK1RT5InQEW1+bVH8gLC9KYvFOXbr7bym129U72UNEYEZVJVxSxBGTEC+SMlJ7CzO8iiCg92W4YEDUBXGw028xdzKGYE2kcxAmB2DQfSPIEG6A+gBvqyLs0KAc2LVSkl3cH4u1Fv/QH17qbsezsGeoMRSr32+PdWcvhA0ZyknIBWIQ1jwvGBdbPWPjg1Y1hGQ8+qKhaTlhQjkD80h8NMugwPxSeHZmoSs1Cd7dQVO7Bp0BIwjUH7QBiHTUsaMZFIqceeJjEZHyQ3ijdgNYotiHkCPYlGoN18nsrTHXhvMBrPBwDUl7hxaHCgsBYtyRMwG8aUlIkK05zOWNjWMgbTCT0WWk5LDOviCUwOHnN+0D5/yJwcmqFJLE5nG66qamqLnCOewGCY6kJHXHcgFZ/HniEnMPYgud5Y+GdBzBNIrBBS1hTSPN2B9wYj8XwAmGOxG1xR9hfNMRvFLErLzVlI4gkI0xwrd2d9nU5k9QQisbVKdVCeiU0S3dVtzvjPZgRUWIfebqisNWcIJXgCmcpDLaxx0knSkhVVZu3vKEbACgfVl7hx2LTkCqGYJ5CvWHwgxRMAmGsb5kDhHLNJLIZmt0NZpVQICdMeyxPoGooQNaaXzGsom76wbt5oSsdwvvEWoIJD7O8NUeqxU54lrEN3BygFVbU0lLho7deJGoqOAT1jZZCFz2MnbCiGIyPCLJrNDjV1qDHCQSVuO067RpnHnmQElGUE+gM5r8yJGor+UJTSBE8AYK7RS7enlH53cfITpFdAOA6wPABDmVN/pxN61sRwLH8hGsN5JiYsc7A3FB8LkZFOM+6tVdXS6HMTMUzxmX7dyJoUBvBZMpOpQ+Bq60edJuoPRuJ5hjKvI8UTaAV7zFj1dI2yuaMnEIqiMBPaiTQPm17Hgf7kPyCzV0DCQcL0pnMwjCc2r3+6hYQsI+BOSwxbRkA8gfziLUQNDdIS0GnyZQ/rqM4j5n9ingDAW61mVdGoRiB2R51an6zVNkBXGyqc+QPpH041AqYRUeEwdHXAgsXmiTkOCQXijWIpnkCfabD2pwrPV1RDb7epgCQI05SOwTAnxkK90y05bCWGXamJYfEEJgfNW0B3xM5wxBjbE3C5oaQ0Pk30rcMDwOhGID5ELpTqCTSAYYBlXFLoGY5QHivTLPc66LESw51HQBloJ50K5L5CqDdhZEQipf4jlBjB+FjpOBVVZpjM353TdQhCrhgKRxnQDZZUF6Ax/TyBUNYS0cn1BLIEwnPL97//fd5++218Ph8PPPAAAAMDA6xdu5bOzk6qqqpYvXo1RUVFk7EcE28hB21mnLtpFCOgutqgqhZN0yhw2qkocLCr2+wwHisnAKT1CmhzGlBgJofrmpIeM5SidzhCWexCXOp10B+KEo4qHLHKIO3Ek1HP/CLnnoDlsaSGg7SAn2YGR1TGrOMV1eY+ujvSdJcFYTrQOWh+pucUuyj3OqadEdCzJIaVZQRmUnXQRRddxJ133pl07Omnn2b58uU8+OCDLF++nKeffnoyljKC1xsfCNdYOpon0AaWkAqmwIwCPA4bxW571qeVxHICqV3D1GQfJNcfihJVxMNBVrK6NxgZSQrXNZmNW7kOB4XSw0HKMKC/l7nOMAd6Q8nVFbGuYUkOC9MVqzKoutBJdZFz+oWD4jmB1D6BmBFwzCAjsGTJkrS7/E2bNnHhhRcCcOGFF7JpU366YLPiLaSlsAaf20ZJlou5Ugo629AS7nQbYl5DTZETLUuPAJg19kUuW7on4PGa5ZUZKoSsJHA8JxC7K/cPR8ykcEkpWkEhlFehcpwY7h2O4rRpFDgTPhKD/RCN0lyooUcVbYl/ROWVoGlSJipMW6w7/+oiJ9WFzmnrCaTpCcyWjuFAIEBZmVl7XlpaSiAQmNwFeAs4WFhDU+EoP4L+XrN7L9EIxJLDo+UDLKxegTSyDJKzxGQSE8NgGgHVdhhq6gDQ8jDP32oUSzJsMUWx5jJzz/t7g/GHNIfTnCfUJUZAmJ50Dppd/aUeO9WFzmnXK6BHxpgdNEnhoEnJCYyFpmmj3lVv2LCBDRs2AHDfffdRWVk5ofdxOBzx5w5X13KoIMoVPlfW19O7juAHfAtOwB07Z1nQCZvamVtZMuY6KotbGYqSdl7fvEUEf/9rKioqkvYd7oh1C9dVUVnqRXlCwH7CDg+2ziO4zvwgvspK+uubGNr8p7Tnj2ff2Rgy2qgs8iSdF2rZTS+wbEEjtoMDdITsSY/31NZDfy/lWV773dY+/nTAz60r5o65xnwwnn3PRGbrviF574FIF7XFbqqrqphfG8XY0o3hKaamJPuImMnE7h7ApkFtdWXS3/GA08kgUFk7x2zMHAfH8jufMiPg8/nw+/2UlZXh9/spKSnJeu7KlStZuXJl/PuuromFQiorK+PP7RiKMuzwUG0MZH09Y/d2APpcBWixc3yaGTapcRtjrqPArjjYG0o7zyitQA0P0bVnJ1ppRfz4wc7YpMNgP11dgxiGQgMOtnawIuAnVFpBV1cXhrcIwjpd+/aglSQL3Yy172x09g1T7nUknWe0HABg2G6nrtjF1lY/XV2FI4+XlKH2bs/62v/z1hFe2hvgsmYPBc7xfZhzyXj2PROZrfuG5L23dA9Q7rXR1dVFgTLvrre3tOOsMT/Dqu0wuD1oZRVZXy+fBPoHcdk1uruTK+yMgB/sDrr9/nG/1nh+53V1dRmPT1k46IwzzmDjxo0AbNy4kTPPPHNS37/FMCeJNtmC2U/qbDfj3pXV8UMlbjs/uHY+F8/3jfkePrc9fZIoCVKTKclh/3AEr8OGJ1Y3bLdplHjs+P1mSapmhYMqYhY/h8nh3mCU0tSu6UDsQ+gro7nMnaFXoAr8XSgjs+ZBa2zOUmvf9IrFCrODzsEw1bEKPit8a1UMARj//k2Mx34wJWsDYoIymUTmw5NWHgqTZATWrVvHV7/6VVpbW/nMZz7DSy+9xHXXXce7777L7bffznvvvcd11103GUuJ0xIxf8gNqj/7SZ1HoLQCLSVBU1XozD52OoFSr4N+3SCSGoeMD5JLTg4nNopZlHsd+PvN+UZWZRHlsVHOOTIChlIEghF8qQnygB88XjS3h3mlHjoGwwzqCRf8ymqIRqG3J+PrHu6PGYH+6TfGV5jZ6FEDfzBKVcwIVBY4zF6BWHGDGuw3Z3Ed2D1lawxlUBUDJlVVDCYpHPT5z38+4/G77rprMt4+IweDGj69nxJ9MOs5qrMdqmqyPj4W1kW1LxRNnk1UWg5ub9ogOX9Co1j8VI8DfyAKmg0qYwnqmBFQ3Z2MbYrGZlA3iCrSPYHenriYTHNstPXB3hAnVZtelFYe6xXo6hgxTDH6QlH6Y41yh/tEgUyYXLpid/yWJ+C02yj3Omi3KoSsi39vD6q/D604ezg6X5gi85k8gck1ArO2Y/jQoKJxsD2uM5yRrja0yok3QsW7hlNHR2haxgqhngyeQJnXgT9ig8rqkamChcVmF3OOPIFUbWGLRIH5ubFeiqTO4ViYTPWkVwhZoSAYUWMThMmiI6FHwKK6aKRMVO1P8AAO7ZvUtVmYIvMZbuPCkycyD7PUCCilaOkP0zjcGVcXSztHD5l3wsfQDWs1XgVSR0cQE5hJMQKmsld6OKhXc2FYoSBiRqSi+phGRyh/N8bTj6Ki0TRt4Th9frSYEagscFDosiUbgfLsCmPW3X9tkVOMgDDpWI1iVYUjf0/VhSMNY+rAbigy7/5VyxQZgYiRMRykwvqkNYrBLDUCXUMRhsIGjWF/XGc4/aSYatYxGAFrBEOm5DC1DdDThQqa8f6hcJRgRFGeOrvHYyeq2RmoTimzLK88pl4B9cbLqOf/G3ZvjfcypHoCJHgCmqYx1+fmYIIR0GIzlTI1jB3u07FrcFpdIa39epKugjq4l+iav0f1TT/dV2Fm0DEYxqZBRUGCJ1DopGsobPYK7N+NdtIpZrhzCj2BrOEg8QTyiyUR2WgMwFAWI3CkBQCtes6E32dkflAGT8CqEIrNBLKmhaaFgwyzeqm3oj7puFZedWzhoFaz/FNt3ZwQDkoYGREcglAwSVu4qdTNgUAoRSgns65Aa79ObbGLJp+bYETRnaiL8Of/g9aDsHvbxNcvCKPQMRim3OvAkVDAUV3kNHUFOnrMv53mhdDYPGWeQNbEsOQE8k9LwAxPNGrDqGzhoO3vmsnbxvkTfp8Cpw2HTUuXmYQ0qcnUkREWZUNmDbG/JCVBXV51TOIy6lDMCGx7h97hKDYNilwJ4aBeqzx0RFt4bqmbQd1IuqBr5VUZu4YP9+nUFbuoj3VYJ+YI1K6tsTVMzR+fMPNJLA+1sL7v2HcQAG3uIrSGeXDk0JSMRM+aGJ7k6qBZaQQOBkL4PHZK3Las4SC1dTOcsNQUpZ8gmma2rKcNkQOonmNW/MTKRC1B+VSFs9KAGZbyF5QlP9+Kx09glLOKRqGtxZS63L+b3oEgJW57ctlrn2kEtARPYK5vpEIoTmU19HSaw+ZiRA3Fkf4w9SUjRsDKC6hIBPbtNP/fsv+o1y4I46FzMBwvD7WwegXaj3SY/T9N86FxHkQjowo9WajgEOqdN3K2Rj2q0gVlwNQYnml9AtONlkBMTcxbkDExrLo7oaMVbckpx/xePo8jc8OY02mWn47lCXSaYSm/LVkDWasYX6+AUip9XkpHK0QiaCs+BMog0N2buTIIkjyBpliFUNJY6Ypq80PbPzL7qWsoTNhQ1JeYI3w9Dm0kOdyyz5zH5PZOWSxWmNlEDUXXUCTNCMR7BXoGoKYezVuA1jgPSE8OJ4U8rWMvPY/x0D2oQ/tzsk49YuDKVB2kh9AmSVAGZqERUErF1cQ0bwHEErNJ52zfDBAXcDkWSj32zEPkAGobksJBTps5eTQRd0cLXkNP9yasXoExjMAv3u3i5l/8OfngYTMUpH3wUnB76B0YTq8Mig2PwzcylqLYbWoxJxoBLTZSOp5IZ+Suv77YhaZp1BW7RjyBPWYoSFvxIehqR2VLzAvCBOkZjmCo9CGPTruNMq+DjqEoWvNC82B1nRl6SbghefSdTv7xN/vTDIHa8Z75dWvK39MEmVUdw9OJ7uFYZZDPDd7CzCWiWzebVS8poi8TweexZ84JEEsOtx1GGdFYt7A9fSBceytlhOLhojilFbFRzqMbgbdaB9jTPUR3gsi2OnzADEU1NMMJy+jVVXplUK8fHA6zJyGBplI3BwMpngDJxihuBGKhoPoSV7x7WO3aBhXVaMtON0/O0V2VIFh0xMtD0y+k1R7otBXCXNMIaHY71DUl3d3/4WA/e3pC7EsYk6Ii4Xghg9r6Tk7WOWpiWKqD8ocVz26Kh4OGk8sXlUJt34x24injmtA5FtY46UzupTb/BDOUsvUd/MFIekgmEoGuNsocJAvOEwsnlYwuLhOKGPEPsqWGBjEjUDMHzeVGO+kUAnYvPlJq+QN+KClL+xk0l7ppCegjISYrLJWQHD7cp1PotMW9i/oSFx0DYUKRKOzZhrbwJGhsNtciISEhx2TqEbCoNobp8JQR9wTADAm17EUpRfdQOD7m5PWDCSNl9u82w5gV1bBry4j61wSJGoqIodIFZUCqg/KNVRnU5HOZnoAyIJQQEmo9CH29kIN8AJieQNhQDEeM9AdPOQuKfRgbf5txbhBdbWAYZtdwJm+ivHLUcNDu7iDWtXpnV8IeDx+AOrPvIHjCyYTsLnyB9qTnqj5/UnmoRZPPlSQwo3kKTG8hoWv4cL9OXYkrbkDqS9wooO3gEdO4LFxiCusUFJk5AkHIIVZDWFVBuidQNdRNl8dHtH7eyMGGeTDQD709vNduhicrChz84WB//ObNCgVp13zCrN45xvLmcOwPM1VQRiklRiDfHAyE8LntlHgcpicASb0Capvp6mkn5sgIuK2GsQy9Ag4n2nkr4d0/4R8Kp1UGWT0EZcXeeB9B0vPLq2AUhbHtsQt/nc8T9wRUKGSqpdWboa7eMnMyaWn7/uQnB7IYgdIMFUIV1ajOtvi3h/t06otHPsRWWOjQnlhp3sKTTAPROC9nSTZBsOgYDOPz2HE70i9v1f5DGJodvzHyt2Ylhzm0j/fahyhy2fjYkgpa+3UOxm4a1c73oX4u2unngt0ev05MFD2SWV+YaASUEiOQT1oCoRFNYW9sNn5CclJt3QzVdSPVN8eIFRJJnR9koV1wOWGl0R9WaZ6ApStcVlFCMGIwHE7xJipi5ZkZQk0AO7qGmVPs5Jy5ZezqDmIoZZaGKoVW3wxAX8h8Td/BbcmvE+hJKg+1aPK50UiuENLmn2C6yMFhghGD7qFI/MIPMKfYvCNrbesxf+axXIvW0AyH92cdRS0IEyFTjwCYd9lVrWZ5cpLecEOz+XiLaQSWVhdwblMxGvB/B/vj+QDtxJNNz3feYvM6cQzoMU8gzVBZ+sJiBPJDYmUQYFYHQXyInIpEYOeWnJSGWsSHyGWYHwSgVdXiX3oOAGXulF9HeysUlVBeYhqr1LwA5VWm69ifLs2plGJH1zCLK70sqS1iOGJwqE+PN4lheQLW3KDedjMURiwJNtCfVB5q4XbYqC12ciAhOayddSHoOuqdP8abwhKNQIHTrCo63B+GBSei2WL7bJxnfug7jmT82QjCROgYTC8PBcDfRbXfrMZrT9Ab1goKoaKajsPttA+EWV5TQJnXwZJqr5kX2L/LLNs8YZl5/pJT4eAeVH/fhNc4Ii2Z4glExAjklc4BfaQyCEbCQVaF0P6dEBo2Z4rkiJHREZk9AYDAGR8CoKxjf9JxS1c4UWs4kdHEZToGw/QGo6YRqDErfHZ1DZvjIhxOs1mNBCMQHhhxcQOxmT4ZPAEwO4eTwkELToTyKtQfN8Yrg+pKkj/E9YU2DlNgJoWt9TdYNdrJ+xaEiaKUomsosyfA/t1UBc3+lzTR+cZ5vBswL8wn15o3XSsaizkQCHFo6y7znBOWAjEjECsgmSiWyHyaEbBE5qU6KD/s6zHv+JtSjIBVq662bjbLLhcvz9l7WkPkMnYNx/DXn2Ceu/m15AfaW9Fq6keMQKohGUVcZkeXmQM4sdJLY5mXQqeNXd1B0xOoa0Sz2ZPW5SstGXFxM3QLJ9Lkc9Par8c/yJrNhnb2BbD1zxzuMu+O6opTjIAxQGtBFSxYMnKwrhFsNmkaE3KGfyiMHlWZw0EHduO0QbnXnhwOwrwheV+rwOe2xSMFK5rMm6fXW4ehoRktNnWU5kVmWPMYSkVD0Swi81Y4yCF9AnlhX7d5sW+M/ZJHcgKmJ6C2b4amBWgptfHHgsOmUeyyjeoJ+HXzA1G27U/xYWwqOGQ2bI3iCYzWMLa9axi3XWNuqRubprGwwsPObtMT0OpHJpIGghGKXDZcJy2Hne+bIbF4o1h2T8BQcCgwUiannXUhGAaHDx6hqsCRFuus6z/CgLOAvrqRWUya02U2zEmFkJAj2vpNDzVTeajavxvq51Jd6Er3BBqaeb90PkuLjHhVW2WBk8UVbt7QqtASbgw1ux1OXI7a+k7WfNxYZPcEzL8pzSUdw3lhX88QPrc9fnc+Eg4aMkc6792R03yAhS/WK5AN/3AEG+DTB1Gv/M482G7GybXaeopdNhw20hvGLHGZ7vQKoR2dwyyq8MTnAS2q8LLfHyLU1wcJRqA3GMXncZghsFAQ9u1EZRgel8jcDOMjtIZmqJ/L4UAwLRQEUHfETMgdSZF01hrmScOYkDOO9JkfsFRPQCkFB3ajzV2YJC4Tf155E92eUpYbybO4VhQOs7eonvbmk5OOa0tONT3wWAXf0WLlBNISw1b/gXQM54d93UMjlUEAbo8Zjhgagl1bIBrNWWloIj5PZsF5C/9whBKPHfvy01B/eAEViYyojtXUxwbROdJzAppmxuJTPAGzSSzI4sqReUMnVHiIKthfVJfkCfQOR8wR0ouXg2Yz8wIBvxkWK/ZlXO+cYhcOm5bcOQxw5gW02oqpdyYbPBUOU7f/XWBEdzhOY7MpVj84itazIIyTEU8g5SLa1Q6D/dC80NQVGAwnzdR6L2zeEC73J2sOr/DvAOD/3I1Jx7Ul5kiZiZaK6tEsieG4ERBPIOcopdjfM0Rjwl2qpmngMYfIqa2bzThcQuIyV5R6HHQMRrK6jlajmO2CK8wL8OY/mXcYmhYXtTEbxjJ4Exl0Bfb0BIkqWFw1YgQWxQzCzpKmeKMYmKpnpR4HWmERNC9Ebdts5gSKSrJOUHXYNBpKXMmD5IDAKecx7PBQ150S3jmwm6qBDhyaSlMZs5LD4g0IuaCtL0Sh00ahK2UWVkxTWJu7iJoiJ1GV7Fm/3zFMWXSIOYeSm8Cqdr/NgmAH/9eecvNSNcfsj5lgXiAUDweJJzBpdA9HGNSj8WanON4CCA6Z+YBFS/ISizu5toCOwXDSLJJE/MGI2Si2/DQor8R45TemESiviq+n3JvuCUBsmmiKEbCaxBI9gXKvg0oVZHfZPCiriB/vDUbiFUzaSafA3h2o9tas+QCLuaXuNCPQ6jSHzc3Z9WbScbVnG3YUcwod6VKTWaY4CsJEaO8PZiwPVft3m7Ow6ptGdAUsqUmleK99iOX2frRD++Jj0VUkDHu2scI7yM7uYHwcBZg3kNqSU2HHe+Zo9qNkTE9AqoNyT1xIxpfyw/UWoDqOwKH9aCeenOGZx865TSXYNXj1QOa64p7hKGVeB5rNjnb+ZbD1HdTO9yBBV7gsixGgvBL6epNmmezsGqa2yJk2i2jhcBs7fXPjia9w1GBQN+LnaSedAoYBO7eMaQSaSt10DZmG1SI+OK5lS1InsNq1FarrqC/zpnsCvjIz7CQVQkIOaOsLUV2UuTKIhnloDmfcCFi9Ai195pTe5WV2c6qwpZS3bxfoOufON3Njb7Qkhyy1JaeajaYxfYyjIdRnXgtS9QRUvDpIjEDOSRocl4i3APZsB3IzOjoTJW47H5hTyCv7+8yu3QSihiIQjFBmXYg/eKmZp+jtQaupi59X5nHQF4oSjqaElOLiMmZyWCnF9q7kfIB1/ISuXbQ7SuiL5ScCoRRt4QUnmncgykDLkhS2aM4wPqK1X8dlg0q9D/WnjfH3tYbG1Re7aBvQ0/UNGudJr4CQE9r6Q2megDIMOLAHa2icVTlkJYffazOrBpc3x/puYl6p2vEeaBp1y5fQXOpOHigHcNIpoGlHHRJSrQcJ/e4ZAJw7UnoNwtIsljcOBkKUep0jlUEWVploQSHMnbiU5Fhc0FxC11CE7Z3J+gV9oSiGGhGT0UorzMFykOYJAARCqQ1jsXn+sZHSnYMR/MORNCOAv5tF3XuAkYmivbF5RPFwkNMFC82GmDE9gZgxTewcPtwXYk6JG9uSU1F/etX8YFR1pgAAGetJREFU42s7bHYfLzyJ+hIXESO9UUdrmAetByfkVguCxYAeZVCPUp1aHtrZZpaBx8ZHO+02yr2OeDjovfYhqgsd1Myfa17UY16pOS+oGa2wmHObitnWOZyUR9AKi2HuwlGTw++3D8VvusAs5zbWfQ3dbl7kHQ99E+PFZ0fyhRIOyh/BiMHCyoK04/HREYuXxxuo8sFZDcW47Bqv7E8OCfkzyEraPnSVubamEaNU5rUnnR8n3itgegI7MuQDADh8gPkDh7ChzH4BSBCYTximZZXIjmEEqgodeB22JE/A0hXWzr7AdKn3bkftjonILFxCfYk7fl4Sjc3mSO2Y1KYgTIT49NBUT2C/2fGbOD66utAsEzWU4v32QZbVFGLzeKGmDtWyHxU28wHaYnNUxIqmYhRZQkJ7d6CGknVJwlHFf/ypja9sOMhXNhxkIBRFDfRhrF0DwSHCZ38Ihw1sp5yJevzHqEe/b/boWB3DkhjOPV/8YD1rP7Is/YGYJ5CvUFD8bZw2zm4o4g8H+4kkhEMyyUpqJ52C7b6foC0a6a61Hs8qLhNLDu/oGsZl12guSw57qdYDeKM6jSXOuCcQiBuBEeOnLTsDNBtagheSCU3TaEpIDkcMc7x0fYkL7dSzweVC/fEV2LMNioqhtj7eP5CtQki0BYRjwUrcpnUL799thlfmjIhEVRc56RwMc6A3RL9usLzGvBk0+1b2xeYF6fEmsSafm4YSV1pISFtyaiyP9l78WPdQmK9sOMD6Xb1c1FxCa7/OPS8fJPjg3dDVju3vvopeUILbbsP2t3egXfmXqFd+i7FuDfTG+hSkRDQ/2DKJxMQ8gVzOC8rG+c0l9IWibD4yctdgjYKw7vQtUqeYZp0fZInLxJJZ27vMJjGHLWWvhw5AaTmLqgrZ2R1EKTUyMiLRE6hvwnbff8LSD4y5n7mlLg4EdJRStA3oGMocHKd5CtBOORv15muonVtggTk6usRtp9htT/cEahvMyo1RKoTeOjzAob7M1VWCANkVxdSBXdA03+z0jVFdaBqBzW3m36JlBGhoNmVP3/mjeXMVmxcEcG5TMe+3D7H29Va2d8bEqOafCC53PC/wfvsQq9fv50CvzpfOr2P1eXXcflY1W7pCfK/gdPibL6ItXoYeNXDZNTSbDdtHP4X26dWwZxtqwzNgsyWtNd9kLgSfRWhnnGdKLSYkYfPFaXOKKHLZeOVAH6fXFwEjd/ZpgjIplHpMkezeDLoClriMHjWbxK49MT2pq1oPQP1cTqjwsmFPgLaBML3BCG67hteZfC+glVeOaz9NPje/2x2gNxhNk5TUzroAtelVGOhDu/CK+HPqi10cTrmYaw4HzGnM6gn8bncvD/2xjWK3nXsvbYoPAFRDg6j1T4CmoV23amQ6qTAr6RwM43bY8LlHLqBKD8HBvaZuRwJWr8DL+/qYU+yMGw6tcR4KUK/9Lp4PsPjIknL6Q1Fe3tfHy/v6mFfm5opFpXzwhFPxbN3Ms9t6ePjPHcwpdnH3ynoafW6UYXD+S/9Fd6viZwuv5qdGGbcqhR5ROBN6BGwrPoSqqsX4/j0wybkxMQJNC9CaFkzKezntGisai3n1QD+hiIHbYcM/HKHQZcssOJ2Aw2beSaeFgzDFZdSh/ezpCRIx0vMBKhqB1ha0i0/mhEoPYCaHe4NRSscwPqOROD6iNUFcHoBlp5nKYUMDaAtGGvDqS1y83TqQvoeGeRkFvP9woI/v/7GN5TUFtARCrHmxhXsvbaTqnY2o/31kZIy2HoLrb82JJKhwfNIxGKG22J30GVDPPQ6hINpp5yada4WM9vlDXLYwoTPeal4cGkRbkRw+LnDa+cxZtXzqA1W8sr+P3+zq5Qd/aufhqutocraw4+0Oznb1cbv9EAWvvYmhDDh0APXWH7juIzfirynjme1+KgocGfWFtYUnYbtr3Zi64blm1huByeaC5hJe2BPgzcMDnDe3xOwWTq1YykJWmcmKKnh3Ezs6MyeFo22HzcRr/VyafG5cdo2d3cMEgpGkfMDRkmgEDvfp+Nx2imJ3YZrDiXbW+aj/ezlelQGmEXhxb5ShcJQCZ8J7N86D/3sJ1deLVmI2nb3dOsB3X2/lxCov/3JRA0f6de787T7WPPln7v7Tw5Q2NWD73BrUGxtRG34F3kK0v7hhwvsRjm86B8PUlnji36uDe1G//V+08y6JJ3gtEkNGy2sKRx4oqzBncg32Jw2NS6TAaeeKRWVcvrCUnd1B1r/byuZgGav2/pqPHHwZDYhn/TQN7fKPol35l9yM6fn/7M+dlLjtGYfcaaUVZp5vEhEjMMksrTYFKzbu7+O8uSX0DEfTZSWzUJq1YcwUl9nR1k91oTMttBQ5uBcArX4uNpvGwnIPO7uCBCMGNRkaa8aLz+Og1GPnQG+IIzFd4US0j92Edsm1Zt4iRn1CcnhRxYix0hqazT+cQ/tgyQfY1jHEva8cptHn5qsXNeAa8NP01M/4ytZ9fO3U/8e/fujL/Ou1J1HsdkDTAnP0x3OPY3gLsF123YT3JBy/dA6GWVpn3kCoaBTjZ/9mjj/5+KfTzk28AMfzAcRGyTQ0w873k/IBmdA0jcWVXhZfvAClN4CxHLTPmrkEm80MM2taPEypAZ9fMYfeYJT324eShJemEgmiTjJ2m8b5c4t5q3WQAT2aWWA+C+Vee+bREbEy0R3dQU5MLQ0FIgf2mB/MOeYQrBMqveztCdIzFD4mTwDMzuGDgRCt/Xrah1rzeNFqk6uMslUIjYyP2M/eniD/+vIhKgucfO3iRgp3vYux5u9Rb77GSR88iy+fX09LxMk9Gw8Tipijf7VP/R3a6eeh/uenGK/+7pj2JBx/BCMGgVCUmuJYvmjDM3BwD7ZP/r+Mo+FddhtlXgcNJa60vz/tvJVoF155VCPlNZfbLIhwe8z/O5xodntansppt3HnBfXML3Mf0w1YLhFPYAq4oLmEZ7b7eaOl/6iMQJnHQW/QHESXFPsur6LL7aNbh8VVnrTnRQ7uhao58TlEiyo8hA1FWFdpoyWOlrk+N+t39RIxVJK4fDbmFDmxaRnKRItKoLSCw4c7+Fp/C16nja9f3EDJK89hPPEw1DVi+9svo9XUcRqwWnPwndda/3979x4U5bkfcPz7vssut4VluQgIKuLtVI2JHjxeqlEDadrExowxTmKdHkdOTJpEYxyp2J7GtGo0VSqZM2Q01sbUadKcdsZMsE3t6DF64qUaCTGHHFHEcJCry3JZYO/v0z8WVxFUFHET3uczw+yy1+e3vLy/fZ/3eX4P7/y2hvWPpmM0GOAXaxBuJ2JfEVpEFPyZPCLQi2sjg1JiwxGNdYjP/i0w6fKnf3zL5/z5OGuv/3vqjHkwY96AtTXaZGD7n2bwQzl9JY8EQmB0fASpMUb++0ILXk30uTvIGhmGTwPHzesVxycFqoPSyyQxwFdVCenXK4eOvaEbxtLPI4ERceHBeQ+9rSNwM6NBZUi0sUcS8GuCY6Pm8Kb6UwD+/tEUEn9dhPiPf4HJ01Dz/7FbGY1ZI2J5ZVoKZ2s72HrsCk2dXpQwI+rL62HUHyH2/BPusyf7FZv041Bpd7HlaA2qAmOTotH2FYEhDPUv/uq2AwWenZDAY5m9l0sfaAZV6X3IegjIJBACiqIwe0Qsl+yBSVt9PhK41YQxcwzl1kxM+MmI634kIDxu/PVXUG4oH50UHRbc+ff3SODGqqx97eNMizVR27WugE8THL7UwmsHKimMmU60p50NkyNJ3fUW4uQRlAVLUF9ahxLRM7n9yeg4VmQl8019J68WX6b4vB3NaEJd+XeQNpyWt/PwF72N+P03d1wBShOCFqevZ10j6QdLCMGBcjt5B6tw+TT+IXsYKaVH4Pw5lIU/R7E+2BOsP1Yh7w4qLS3lgw8+QNM0srOzeeYZfRzCP5oRy69/F5gd2Nd++WtJ4NokL69f8G1DByf+4OB4chaj22sw/Nc3iKxZKEO7ZkfWXQFNQ0m7PltSURTGJkRwpqaj30ngWlVWVYEUc9+TwLcNnRy82MJ/ljXR2OFlpDWcv05t5Wcf70D9XSRoAvWVv0GZPP22r/XUOCtThkbz/pkG/vlsI4crW3lpajI/WbORiN8epPPgfrTSUzB0OMpj82mfMpvvOwLF7uocXuocbupaXNR3+PAIhXD8jMbBWM9VxnTWMbativi2RogyB1ZPS8/ouhyJEhPbr89Oundtbj+/OlXH6SvtTE2LZtX0VGLcDhx7fxUoCf/oE6Fu4o9GSJOApmns2bOHX/7ylyQkJLB+/XqysrJIT08PZbMeiGGWcEZaw7nc7O5zd9C1x52sdnDkcitnatrp8GhEhqlkxas8W1GKOHAcUfzvkDYiMBHu2hfbtIxurzU2IZIzNR397g6KMhpI7urnN95cG/0W0mJNePyC907XMyYhghVZyWSlRUNjOBoCzLGor/5ttxXQbic1xsSb89I5Vd3O7rMN5P/vH8gZZeHF+T/n9xNyqDhXTsWVJiovxtJ4pTr4PKPmI8XVREqnjYedTSS5mmmITORCXAbF0Zn44sZAHCQJJ8M8doa01jOkuoIhrtMkuZoZYhKYEpOwRydij7RiD7fQZDTTZIjCgRF8PlS/D8XvRfEFflSfF6vmIhEXibhJUD0MUbxEGVWIikaYLXhjLLij4nBGxuKONKMZjJgUgRENo/BjVDSM+AlTQDVFBEoimEyBUgMPsOZMqJQ1dFJwvJZWt49fPGzlqRERKG4H2se7wOVC/cvX5MTBuxDSJFBRUUFKSgrJyckAzJw5kzNnzugiCQA8PiqOfy29SkJU3/5xrZGBWcP/c7EFs0llWnoMM4fF8HBqVNdks4cQLXZEyYlAyYbPPgYhAiumDUnt9lqPjbLg9guG9uFk7p3kZFq4m06Un6XHUG5zMXtEDJNTo6/32yYPRV2zMTDF/y5GZkDg6GbG8BgeSY3mk29tfHbezqFLZ7vutZCckshok4cn6r9j5IX/I93oJT4xDkNyGoxLQ0kZF6jaGmNBUdWu2dduym1Oym1OatviuBAzjPYk7daN0AA3RHs7ifVeKw2ioKkmhBqJFqbiM4bRpoajKd13UpF+N4pL4PKa0FpuvK/nxLobqcKFQfgxaFrgUmgYhIamqGiKgqao+BUVTVERKKhd96towesGTUNBoBAYxojC9esIlJu70rr9rlx74PW7g7cpgdm31x5w7aLr+TdM6QIReHTgvsClQEEooKEiFAU/CkJRaDbFkuxsYst3HzHqNzVd7xEQvWQFrhR97D/uF0XcqbN0AJ06dYrS0lJefvllAI4dO8bFixfJzc3t9rhDhw5x6NAhALZu3YrH4+nxWn0RFhaGz3frtX4fNCEEDreP2Ii+f3s7WmEj0mhgSrqFsDvMMvY3XcV94jcYzDGEz3uyv839Uals6uDrGgcj4iIYO8RM7A3dXj1GV92FDrePeoebujYXdW1u3D6NJLOJxGgTSeZwEiNVIjxOhMeNEmVGiYzq8V4+TdDU4aHB4abR4aah3c3VdjcKChGqIMLvJsLnItzjJNzVgaL58GHAoxjwoOJDxYOCVwOfz4/P78ffdenza2iaQBHXd/KqEKgisKMXKPhvSAz+rt+FCHwuN/8AgeHFKASHs3SLR9wwM0ogAEUEriuBDzuYTOj+rK6/RdfrKYEdPKgI5fptKoETl6oiUAOtINHg47mYFqJNYWAIC5QdCTOiWuKInvkY/tDt0kKmL/s20y3KU4f8nEBf5OTkkJNzvfaHzWa7p9dJTEy85+cOJNvtv+x1MyEOwE9Ls70Pj1ZgRvYPNu6BFAs8OykFm82Gp73lrj7jO7EAllj4SbcT4T7w++hsh8ASJQbodAZ+emEAhppgaIICCRFAz6G990ovf+/ePtkIIXQR+8368jcfOrT3+mgh7TiLj4+nqakp+HtTUxPx8bdf0UqSJEm6f0KaBEaNGkVdXR2NjY34fD5OnDhBVlZWKJskSZKkKyHtDjIYDCxfvpzNmzejaRrz5s1j2LBhoWySJEmSroT8nMCUKVOYMmVKqJshSZKkS3IwrSRJko7JJCBJkqRjMglIkiTpmEwCkiRJOhbSGcOSJElSaOnqSCA/Pz/UTQgJGbe+6DVu0G/s/YlbV0lAkiRJ6k4mAUmSJB0zvPXWW2+FuhEPUmZmZqibEBIybn3Ra9yg39jvNW55YliSJEnHZHeQJEmSjskkIEmSpGMhLyD3oOhlQfv33nuPkpISLBYLBQUFALS3t7Njxw6uXr1KUlISb7zxBmazOcQtvb9sNhtFRUW0tLSgKAo5OTk8+eSTgz52j8fDhg0b8Pl8+P1+pk+fzuLFi2lsbKSwsBCHw0FmZiYrV64kLGzw/btrmkZ+fj7x8fHk5+frIu5XX32ViIgIVFXFYDCwdevW/m3nQgf8fr947bXXRH19vfB6vWLt2rWiuro61M0aEGVlZeLSpUtizZo1wdv27dsn9u/fL4QQYv/+/WLfvn2hat6Asdvt4tKlS0IIITo7O8WqVatEdXX1oI9d0zThdDqFEEJ4vV6xfv16UV5eLgoKCsSXX34phBBi165d4uDBg6Fs5oApLi4WhYWFYsuWLUIIoYu4X3nlFdHa2trttv5s57roDrpxQfuwsLDggvaD0fjx43t8Azhz5gxz5swBYM6cOYMydqvVGhwdERkZSVpaGna7fdDHrigKERGBpSn9fj9+vx9FUSgrK2P69OkAzJ07d9DFDYGVCEtKSsjOzgYCayTrIe7e9Gc7H1zHSbdgt9tJSEgI/p6QkMDFixdD2KIHq7W1FavVCkBcXBytra0hbtHAamxs5PLly4wePVoXsWuaxrp166ivr+eJJ54gOTmZqKgoDAYDEFjG1W7vy5rUPy579+5l6dKlOJ2B1YYdDocu4gbYvHkzAI8//jg5OTn92s51kQSk6xRFQVGUUDdjwLhcLgoKCli2bBlRUVHd7hussauqyrZt2+jo6GD79u3U1taGukkD7uzZs1gsFjIzMykrKwt1cx6ojRs3Eh8fT2trK5s2beqxgPzdbue6SAJ6X9DeYrHQ3NyM1WqlubmZ2NjYUDdpQPh8PgoKCpg9ezbTpk0D9BM7QHR0NBMmTODChQt0dnbi9/sxGAzY7fZBt72Xl5fz1Vdf8fXXX+PxeHA6nezdu3fQxw0EY7JYLEydOpWKiop+bee6OCeg9wXts7KyOHr0KABHjx5l6tSpIW7R/SeEYOfOnaSlpTF//vzg7YM99ra2Njo6OoDASKFz586RlpbGhAkTOHXqFABffPHFoNvelyxZws6dOykqKmL16tVMnDiRVatWDfq4XS5XsPvL5XJx7tw5hg8f3q/tXDczhktKSvjwww+DC9ovXLgw1E0aEIWFhXz33Xc4HA4sFguLFy9m6tSp7NixA5vNNiiHSQKcP3+eN998k+HDhwcPhV944QXGjBkzqGOvqqqiqKgITdMQQjBjxgwWLVpEQ0MDhYWFtLe3M3LkSFauXInRaAx1cwdEWVkZxcXF5OfnD/q4Gxoa2L59OxAYCDBr1iwWLlyIw+G45+1cN0lAkiRJ6kkX3UGSJElS72QSkCRJ0jGZBCRJknRMJgFJkiQdk0lAkiRJx2QSkKQBtHjxYurr60PdDEm6JV3MGJYkCJTgbWlpQVWvf/eZO3cuubm5IWxV7w4ePEhTUxNLlixhw4YNLF++nBEjRoS6WdIgJJOApCvr1q1j0qRJoW7GHVVWVjJlyhQ0TaOmpob09PRQN0kapGQSkCQCJQYOHz5MRkYGx44dw2q1kpuby0MPPQQEKtHu3r2b8+fPYzabWbBgATk5OUCgiuenn37KkSNHaG1tJTU1lby8PBITEwE4d+4cb7/9Nm1tbcyaNYvc3Nw7FviqrKxk0aJF1NbWkpSUFKyMKUn3m0wCktTl4sWLTJs2jT179nD69Gm2b99OUVERZrOZd999l2HDhrFr1y5qa2vZuHEjKSkpTJw4kQMHDnD8+HHWr19PamoqVVVVhIeHB1+3pKSELVu24HQ6WbduHVlZWTzyyCM93t/r9fLiiy8ihMDlcpGXl4fP50PTNJYtW8bTTz89aMudSKEjk4CkK9u2bev2rXrp0qXBb/QWi4WnnnoKRVGYOXMmxcXFlJSUMH78eM6fP09+fj4mk4mMjAyys7M5evQoEydO5PDhwyxdujRY0jcjI6Pbez7zzDNER0cHq3x+//33vSYBo9HI3r17OXz4MNXV1SxbtoxNmzbx/PPPM3r06IH7UCRdk0lA0pW8vLxbnhOIj4/v1k2TlJSE3W6nubkZs9lMZGRk8L7ExEQuXboEBEqTJycn3/I94+LigtfDw8NxuVy9Pq6wsJDS0lLcbjdGo5EjR47gcrmoqKggNTWVLVu23FWsktQXMglIUhe73Y4QIpgIbDYbWVlZWK1W2tvbcTqdwURgs9mCdd0TEhJoaGhg+PDh/Xr/1atXo2kaK1as4P333+fs2bOcPHmSVatW9S8wSboNOU9Akrq0trby+eef4/P5OHnyJDU1NUyePJnExETGjRvHRx99hMfjoaqqiiNHjjB79mwAsrOz+eSTT6irq0MIQVVVFQ6H457aUFNTQ3JyMqqqcvnyZUaNGnU/Q5SkHuSRgKQr77zzTrd5ApMmTSIvLw+AMWPGUFdXR25uLnFxcaxZs4aYmBgAXn/9dXbv3s1LL72E2WzmueeeC3YrzZ8/H6/Xy6ZNm3A4HKSlpbF27dp7al9lZSUjR44MXl+wYEF/wpWkO5LrCUgS14eIbty4MdRNkaQHSnYHSZIk6ZhMApIkSTomu4MkSZJ0TB4JSJIk6ZhMApIkSTomk4AkSZKOySQgSZKkYzIJSJIk6dj/AxnLikdTipNJAAAAAElFTkSuQmCC\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 299
        },
        "id": "30FcTwEWDHTO",
        "outputId": "b1e4411b-1964-4381-ad90-aa447b5e78cc"
      },
      "source": [
        "plt.style.use(\"ggplot\")\n",
        "plt.figure()\n",
        "plt.plot(np.arange(0, 50), H.history[\"acc\"], label=\"train_acc\")\n",
        "plt.plot(np.arange(0, 50), H.history[\"val_acc\"], label=\"val_acc\")\n",
        "plt.title(\"Accuracy Plot\")\n",
        "plt.xlabel(\"Epoch #\")\n",
        "plt.ylabel(\"Acc\")\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAEaCAYAAAD+E0veAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOy9e5QlZXX//Xnq3M/p+2Wm59ojw1UIODDCMFyUMCFqlEXyisYsREBfScwPYy5vjIhLXzVL8hp+mBCTeBkGLzEafwR/AgrJiPyQIQkgTkQHYYZhuufSM32/nUudU1XP+8dTVafqVJ3uM9093Q1d37VYzKmqU/VUn6pnP3t/9/5uIaWURIgQIUKECIC21AOIECFChAjLB5FRiBAhQoQILiKjECFChAgRXERGIUKECBEiuIiMQoQIESJEcBEZhQgRIkSI4CIyChEivAaxadMmPvvZzy71MCK8ChEZhQjLHkePHiWVSrF27VoMw1jq4Sw5PvWpTyGEQAiBpmmsW7eO97znPfT19c35nEeOHEEIweOPP75wA43wqkRkFCIse+zcuZO3v/3ttLW18eCDDy71cACoVCpLev1NmzYxMDDAkSNH+PrXv86zzz7LO97xDkzTXNJxRXj1IzIKEZY1LMti586d3HTTTbzvfe/jy1/+cuCYwcFBbr75ZlavXk06neass87i3nvvdfe//PLLvPOd76Sjo4NsNsv555/PQw89BMB9991HPB73na921fz4448jhODhhx/m8ssvJ51O89WvfpWxsTFuuOEGNm7cSCaT4ayzzuKuu+6iViTgO9/5DhdddBHpdJrOzk7e+ta3MjY2xn333UdbWxuFQsF3/Kc//WnOOOOMwHm8iMVi9PT0sHbtWq6++mo+9alP8fzzz3PgwIHQ46emprj11lvp7u4mlUqxdetW/u3f/s3dv2HDBgCuuuoqhBBs2rSp7rUjvLYRGYUIyxo//OEP0XWdt771rbz3ve/lRz/6EYcOHXL3F4tF3vSmN/Hf//3f/NM//RP79u3jnnvuIZvNAnD8+HG2b9/O+Pg43//+93n++ef5zGc+g6ad/KP/p3/6p3z0ox/lhRde4B3veAe6rnPeeefxve99j3379vGJT3yCT37yk9x3333ud3bt2sUNN9zAddddx3PPPcePf/xj3vKWt2CaJu9+97sRQvDd737XPd6yLO69914+8IEPIIRoeGyZTAao78HccsstPProo3zzm99k7969XHbZZbz97W/nV7/6FQDPPfccAPfffz8DAwM888wzJ/vnifBagYwQYRnj2muvlX/yJ3/ifv7N3/xN+fGPf9z9/NWvflWmUil5+PDh0O/fcccdcvXq1XJ6ejp0/65du2QsFvNtO3z4sATkj3/8YymllD/+8Y8lIL/+9a/POt4Pf/jDcseOHe7nDRs2yD/8wz+se/xtt90mL7vsMvfzI488IhOJhDxx4kTd73zyk5+Umzdvdj/39fXJiy++WG7YsEGWy2UppZS9vb3yM5/5jJRSyv3790tAPvzww77zbNmyRd58882h9xxh5SLyFCIsWxw9epSHH36Ym266yd32vve9j3vvvdclnH/605/y+te/nvXr14ee46c//Snbt28nl8vNezwXX3yx77NlWdx555284Q1voKuri6amJv7xH//RJXwHBwc5fPgw11xzTd1z3nrrrezZs4cXXngBgK985Stce+21rFq1asaxHDx4kKamJrLZLL29vUgpeeCBB0gkEoFj9+3bB8CVV17p237llVfyy1/+cvYbj7CiEJ/9kAgRlgY7d+7ENE22bNni226aJg8++CC//du/Pe9rhIWR6oVgag3LXXfdxec+9znuvvtutmzZQnNzM3fffTcPP/xww9c/99xzufzyy/nKV77CX/zFX/D973/f5TtmwoYNG/jRj36EpmmsWbPGDR9FiDBfRJ5ChGUJh2C+/fbb2bt3r++/97znPS7hfNFFF7Fv3z6OHDkSep6LLrqIp556inw+H7p/1apVmKbJiRMn3G1OfH02PPHEE7zlLW/hlltuYcuWLZx++uns37/fd+7169f7CN0w3HrrrXz961/ny1/+MuvWreM3fuM3Zr12IpHg9NNP57TTTpvVIJx77rnueGvHf9555wGQTCYBouylCBGnEGF54qGHHpJCCNnX1xfY9+ijj0pN0+Qrr7wi8/m8PPPMM+WWLVvkv//7v8uDBw/K3bt3y29/+9tSSimPHTsmu7u75dVXXy2ffPJJefDgQfnggw/KH/zgB1JKKUdGRmRzc7O86aab5EsvvSR/+MMfyvPPPz+UU6jlLf70T/9Urlq1Sj722GPyxRdflB//+MdlS0uL7O3tdY/5yle+IuPxuPz0pz8t9+3b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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N848L5hGDJ1K",
        "outputId": "23458a66-ce05-45c8-d555-d7d825834baa"
      },
      "source": [
        "from sklearn.metrics import classification_report\n",
        "\n",
        "pred = model.predict(x_val)\n",
        "labels = (pred > 0.5).astype(np.int)\n",
        "\n",
        "print(classification_report(y_val, labels))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       1.00      0.05      0.09        21\n",
            "           1       0.50      1.00      0.67        20\n",
            "\n",
            "    accuracy                           0.51        41\n",
            "   macro avg       0.75      0.52      0.38        41\n",
            "weighted avg       0.76      0.51      0.37        41\n",
            "\n"
          ]
        }
      ]
    }
  ]
}