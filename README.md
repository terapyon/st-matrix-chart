# st-matrix-chart

# Streamlit Demo Application (English)

- Name: st-matrix-chart
- Purpose: Display a two-dimensional matrix in Streamlit
- Features: Select columns from Excel data to visualize a two-dimensional matrix similar to a priority matrix

## Setup

### Requirements

- Python 3.11 (or 3.8 and above)
- Streamlit 1.31 or higher
- npm or yarn (node v18 or later)

### Virtual Environment

Install using a virtual environment (venv), which is included in Python's standard library.

https://docs.python.org/3/tutorial/venv.html

```sh
% cd (your chosen folder)
% python3 -m venv venv
% source venv/bin/activate
```

### Installation

```sh
(venv) % git clone https://github.com/terapyon/st-matrix-chart.git
(venv) % st-matrix-chart
(venv) % pip install -r requirements.txt -c constraints.txt
```

## How to Run

```sh
(venv) % streamlit run st_matrix_chart/streamlit_app.py
```

## Viewing the Application

Upon launching, the default browser will open automatically for you to view the application.

If the browser does not open automatically, copy the URL with the port number displayed in the console and paste it into your browser.


## Build

```sh
% nvm use v20
% npm install
```

```sh
% npm run dump st_matrix_chart -- -r requirements.txt
% npm run serve
% npm run dist -- -win
```

## Release

- Create a tag: git tag v1.0.0
- Push the tag: git push origin v1.0.0
- Create a release using the web UI by making a release for v1.0.0


# LICENCE

This package is under MIT License.
Please see [LICENSE](LICENSE) file.



# Streamlitデモアプリ (日本語)

- 名称: st-matrix-chart
- 目的: Streamlitで二次元のマトリックスを表示する
- 機能: Excelのデータから列を選択し、プライオリティ・マトリックスのような二次元可視化を行う

## セットアップ

### 必須条件

- Python 3.11 (3.8以上)
- Streamlit 1.31以上
- npm or yarn (node v18以降)

### 仮想環境

venvを用いてインストールを行います。
venvは、Pythonの標準ライブラリです。

https://docs.python.org/ja/3/tutorial/venv.html


```sh
% cd (任意のフォルダ)
% python3 -m venv venv
% source venv/bin/activate
```

### インストール

```sh
(venv) % git clone https://github.com/terapyon/st-matrix-chart.git
(venv) % st-matrix-chart
(venv) % pip install -r requirements.txt -c constraints.txt
```

## 起動方法

```
(venv) % streamlit run st_matrix_chart/streamlit_app.py
```

## 表示確認

起動すると、デフォルトブラウザが立ち上がり表示確認ができる。

もし、ブラウザが立ち上がらない場合は、コンソールに表示されるポート付URLをブラウザで呼び出す。


## ビルド 

```sh
% nvm use v20
% npm install
```

```sh
% npm run dump st_demo_ai_comp -- -r requirements.txt
% npm run serve
% npm run dist -- -win
```

## リリース

- tagを作る `git tag v1.0.0`
- tagをPush `git push origin v1.0.0`
- リリースを作る。Web UIでリリースを v1.0.0 を作る

# LICENCE

This package is under MIT License.
Please see [LICENSE](LICENSE) file.
