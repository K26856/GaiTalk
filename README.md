# 概要
- 音声合成サービスと、生成系AIによる応答サービスをラップしたサービス

# 入れ方
1. python 3.11.4 環境を構築する
2. gitから全ファイルをダウンロード
    - 例 : git clone
    - 例 : zipファイルでダウンロード
    - :
3. 必要なpythonモジュールをインストール
    - `pip install -r requirements.txt`
4. ラップしているサービスに必要な動作ファイルをインストール
    1. voicevox
        - [voicevox_core](https://github.com/VOICEVOX/voicevox_core/releases/tag/0.14.4)
        - 上記サイトよりダウンローダを取得
        - 上記サイトREADMEを参考に必要ファイルを手元にダウンロード
        - `voicevox_core`というディレクトリにダウンロードされるので、プロジェクト直下に中身のファイルを移動
        - ディレクトリ構造
            - `GaiTalk`
                - `config/`
                - `model/`
                - `open_jtalk_dic_utf_8-1.11/`
                - `.gitignore`
                - `aitalk.py`
                - :
    2. pytorch
        - [pytorch](https://pytorch.org/get-started/locally/)
        - 上記のサイトを参考にインストール
5. 必要なconfigファイルを作成
    1. `./config/settings_template.json`ファイルをコピーし`settings.json`にリネーム
    2. `settings.json`ファイルの空欄の設定を埋める

# 起動方法
```sh
python main.py
```
