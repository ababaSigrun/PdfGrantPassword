# PdfGrantPassword


importフォルダにいれたpdfをoutputフォルダにパスワードをつけて作成する。


パスワードはファイル名passwordフォルダのpasswordList.txtにファイル名の一部を記入してください。


(例)

123456_山田太郎.pdfファイルの場合

以下のようにpasswordList.txtに入力

```
123456=password

または
123456_山田太郎=password

または
山田太郎=password
```


対応している暗号化アルゴリズムはRC4のみ。

AESで暗号化されたファイルは復号（パスワード解除）できない。


テストまだ

パスワードロック部分をパスワード解除にすればそのまま使えるんじゃ・・・
