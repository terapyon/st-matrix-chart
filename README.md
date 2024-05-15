# st-matrix-chart

# Streamlitデモアプリ

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
