Nakamuratamara
====

## Overview / 概要

- This web application made for close university professor. To sharing reports with one's fellow students.
  - 親しい大学の先生のために作った学生向けレポート共有Webアプリです。

## Description / 説明
### Functional Configuration / 機能構成

- Administrator Features / 管理者向け機能
    - Authentication / 認証
        - Login URL Request / ログインURLリクエスト
        - Login / ログイン
        - Logout / ログアウト
    - Report Maintenance / レポートメンテナンス
        - Search / 検索
        - Sort / ソート
        - Paging / ページング
        - Report Create / レポート登録
        - Report Delete / レポート削除
        - Report Download / レポートダウンロード
    - User Maintenance / ユーザーメンテナンス
        - Search / 検索
        - Sort / ソート
        - Paging / ページング
        - User Create / ユーザー登録
        - User Update / ユーザー更新
        - User Delete / ユーザー削除
    - Access Log Browsing / アクセスログ閲覧
        - List / 一覧
        - CSV download / CSVダウンロード
- Student Features / 学生向け機能
    - Login / ログイン
    - List / 一覧
    - Change list / 一覧切り替え
    - Report Download / レポートダウンロード

### Technical Elements / 技術要素
 - Front End / フロントエンド
   - JavaScript
   - jQuery
   - Ajax
   - Stylus
   - HTML
 - Server Side / サーバーサイド
   - Python
   - Python Web Framework : Django
   - SQL
   - PostgreSQL
   - Google Drive API
   - Sendgrid API

### Using API Features / APIを使っている機能
 - Authentication for Administrator.  
   - 管理者向けの認証
 - Report file management.
   - レポートファイル管理

>Authentication for Administrator.

In Japan of recent date, Security incidents are occurred. Some cases, There was a leak of id and password. For example Home file service. So I design authentication feature without id and password.

Everytime administrator request onetime loginurl with his or her email input. Then email include onetime loginurl is send by Sendgrid API.

最近の日本では、セキュリティ事故が起きています。いくつかのケースでは、IDとパスワードが漏れています。そういった諸々もあって、IDとパスワードを使わない認証処理を設計しました。

常に管理者は、メールアドレスを入力してもらって一時的なログインURLを要求してもらいます。すると、一時的なログインURLが含まれたメールがSendgrid APIを利用して送信されます。

>Report file management.

Nowadays we can choose storage. AWS, Azure, GCP. But that costs money. Even if insignificant. So I design report file management with Google Drive API.

Report files are uploaded to indivisual google drive. For example, mine or professor storage.

今日では、私たちはAWSやAzure, GCPといったサービスのストレージを選択することが出来ます。しかし、微々たるものとはいえ、お金がかかります。そのためGoogle Drive APIを使ったレポートファイル管理を設計しました。

レポートファイルは、個人のGoogleドライブにアップロードされます。例えば、私や教授のGoogleドライブにです。

### Architecture / アーキテクチャ
 - Layerd Architecture x CQRS like I usually do. I usually developing web application by Java or C#.
   - 自分が普段JavaやC#でやっているようなレイヤードアーキテクチャとコマンドクエリ責務分離を掛け合わせた感じで作っています。

## Directory Structure Sumary / ディレクトリ構成概要

[Abour this directory.](https://github.com/TsJazz27Sumin/nakamuratamara/tree/master/songcycle/apps/student)

- decorators
  - Decorator for logging and authorization process.
    - ログ出力と認可処理用のデコレーターを配置している。
- forms
  - Classes for forms in html.
    - HTML上のフォームに対応するクラス群を配置している。
- functions
  - Commonly used logic is called from mutiple class.
    - 複数のクラスから共通利用されるような処理を配置している。
- models
  - Models corresponds to tables in database.
    - DBのテーブルに対応するモデルクラスを配置している。
- queries
  - Second Layer : Search process. That corresponds to Query of CQRS. To take charge of select database access.
    - 【2層目】検索を取り扱う。CQRSのQueryに対応させている。検索のDBアクセスを担当する。
- repositories
  - Third Layer : To take charge of insert, update, delete database access. 
    - 【3層目】登録・更新・削除のDBアクセスを担当する。
- services
  - Second Layer : To take charge of business logic about insert, update, delete procss. That corresponds to Command of CQRS.
    - 【2層目】ビジネスロジックを担当する部分。登録・更新・削除を取り扱う。
        - CQRSのCommandに対応させている。
- templates
  - HTML Templates.
    - HTMLテンプレートを配置している。
- templatetags
  - Functions for view process in html templates.
    - HTMLテンプレートで使用される表示処理用の関数群を配置している。
- views
  - First Layer : That corresponds to Controller of MVC. In django, that is called View.
    - 【1層目】MVCで言う所のController、DjangoではViewと呼ばれる。

## Requirement / 必要条件
 - Please use Linux OS. [Because Windows OS has issue about python.](https://github.com/django-helpdesk/django-helpdesk/issues/621) I tried to use ajax in django. But don't work except JsonResponse. 
   - Linux OSを使用してください。Windowsでは、Pythonについて課題があります。DjangoでAjaxを試してみたのですが、JsonResponseを除いて動作しませんでした。
 - My development environment is Mac OS : Mojave.
   - 自分の開発環境は、Mac OSのMojaveです。

## Author

[TsJazz27Sumin](https://github.com/TsJazz27Sumin)

## Reference Documents / 参考資料

For English-speaking countries : I living in japan, I usually use japanese.
So Japanese documents are listed.

- 命名ルール
  - [Python命名規則一覧](https://qiita.com/naomi7325/items/4eb1d2a40277361e898b)

- ログイン関連
  - [Django2.1.1 を使ってログインを実装する](https://developer-collaboration.com/2018/10/05/django-login01/)
  - [Djangoでログイン認証できるようになるまで](https://codelab.website/django-login/amp/)
  - [Djangoのログイン処理を実装する方法①](https://intellectual-curiosity.tokyo/2018/11/13/django%e3%81%ae%e3%83%ad%e3%82%b0%e3%82%a4%e3%83%b3%e5%87%a6%e7%90%86%e3%82%92%e5%ae%9f%e8%a3%85%e3%81%99%e3%82%8b%e6%96%b9%e6%b3%95%e2%91%a0/)
  - [Djangoでログイン機能を作る](https://e-tec-memo.herokuapp.com/article/19/)
  - [【Python・Django入門】ログイン画面、ユーザー登録画面を作る①](http://mizzsugar.hatenablog.com/entry/2018/06/28/215117)
  - [Djangoでログイン画面を作成する](https://narito.ninja/blog/detail/40/)
  - [djangoでログイン画面を実装する](https://qiita.com/hayata-yamamoto/items/cb217f2c6ec07f2dc73a)

- スコープ関連
  - [Pythonのクラスメンバのスコープまとめ](https://qiita.com/0xfffffff7/items/6ef16e79fe9886acb3f2)

- フォーム関連
  - [Django forms.Formを用いたフォームの作成](https://qiita.com/peijipe/items/009fc487505dfdb03a8d)
  - [お問い合わせフォームの作り方【かみ砕いて説明します】](https://codor.co.jp/django/how-to-make-contact-form)
  - [フォームの内容を保持する（テンプレートファイルに変数を渡す方法）](https://narito.ninja/blog/detail/45/)
  - [Djangoにおけるクラスベース汎用ビューの入門と使い方サンプル](https://qiita.com/felyce/items/7d0187485cad4418c073)
  - [How to get the submitted value of a form in a Django class-based view?](https://stackoverflow.com/questions/25090003/how-to-get-the-submitted-value-of-a-form-in-a-django-class-based-view)
  - [Djangoのrequest.POSTからの値取得 - name属性が同じinputが複数ある場合](http://y0m0r.hateblo.jp/entry/20120625/1340631834)

- モデル関連
  - [Django: モデルフィールドリファレンスの一覧](https://qiita.com/nachashin/items/f768f0d437e0042dd4b3)
  - [モデルmodels.DateTimeFieldに現在の時間を挿入する方法](https://sleepless-se.net/2018/06/09/django%E3%83%A2%E3%83%87%E3%83%ABmodels-datetimefield%E3%81%AB%E7%8F%BE%E5%9C%A8%E3%81%AE%E6%99%82%E9%96%93%E3%82%92%E6%8C%BF%E5%85%A5%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/)

- リクエストパラメータ関連
  - [Django でクエリ文字列（クエリストリング）を取得する](https://qiita.com/shinno21/items/f78c4e3580d9cf58b953)
  - [DjangoでGETリクエストのクエリパラメータを取得](https://qiita.com/RyoMa_0923/items/8b13fefc5b284677dfe1)
  - [DjangoのビューとHttpRequestオブジェクト](https://hombre-nuevo.com/python/python0044/)
  - [user-agents](https://pypi.org/project/user-agents/)

- セッション
  - [Djangoでセッションを使用する](http://python.zombie-hunting-club.com/entry/2017/11/06/222409)
  - [Djangoユーザセッション管理機能を実装してみた。](https://sinyblog.com/django/user_session/)
  - [Djangoのセッション設定](https://intellectual-curiosity.tokyo/2018/11/10/django%E3%81%AE%E3%82%BB%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3%E8%A8%AD%E5%AE%9A/)

- ページ遷移関連
  - [【Django】renderとreverse_lazyの使い分けについて](https://qiita.com/frosty/items/1df28edde34907f53bea)
  - [Django shortcut functions](https://docs.djangoproject.com/en/2.2/topics/http/shortcuts/)
  - [JavaScriptでURLを操作するメモ](https://qiita.com/PianoScoreJP/items/fa66f357419fece0e531)

- css関連
  - [Glyphicons](https://getbootstrap.com/docs/3.3/components/)
  - [Python Django チュートリアル(6)](https://qiita.com/maisuto/items/86add9263a641899b1e3)
  - [Django2でStylusを使う](https://blog.takao-hayashi.org/posts/django2%E3%81%A7stylus%E3%82%92%E4%BD%BF%E3%81%86/)
  - [django-static-precompiler 1.8.2](https://pypi.org/project/django-static-precompiler/)
  - [Stylus入門](https://qiita.com/kubotak/items/18abd6eba7e3daaba054)
  - [レスポンシブ対応サクッとまとめ](https://qiita.com/ymtm_jp/items/e8c55046429438a91903)

- javascript関連
  - [jQueryでイベントが発火しないときの簡単な対処法](https://pisuke-code.com/jquery-solution-for-event-unfired/)
  - [jQuery FormでPOST/GETの内容をたった一行で取得する方法](http://www.searchlight8.com/jquery-form-ajax-post-get/)
  - [Django Compressor + Babel で Django でも簡単に ES6 コードを扱う方法](https://blog.ymyzk.com/2015/05/django-compressor-babel-ecmascript-6/)
  - [Node.js / npm をインストール (Mac環境)](https://qiita.com/PolarBear/items/62c0416492810b7ecf7c)
  - [ES2015(ES6) 入門](https://qiita.com/soarflat/items/b251caf9cb59b72beb9b)

- Ajax関連
  - [django – AjaxでレンダリングされたHTMLを返す](https://codeday.me/jp/qa/20190221/287560.html)
  - [DjangoでAjaxする時の注意点](https://qiita.com/yat1ma30/items/c7545896295761a34c77)
  - [Djangoで、Ajax](https://narito.ninja/blog/detail/88/)
  - [AjaxにおけるprocessDataとcontentTypeについて](https://ryoutaku-jo.hatenablog.com/entry/2019/01/16/224131)

- ORM関連
  - [Djangoで素のSQLを実行する方法](https://intellectual-curiosity.tokyo/2018/12/12/django%E3%81%A7%E7%B4%A0%E3%81%AEsql%E3%82%92%E5%AE%9F%E8%A1%8C%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/)
  - [Django データベース操作 についてのまとめ](https://qiita.com/okoppe8/items/66a8747cf179a538355b)
  - [DjangoでIN演算子を使ったクエリを生成する方法](https://qiita.com/nakkun/items/86a94e65fe6785325f54)
  - [DjangoのモデルでLimit,Offset,filterを利用してを値を取得する方法](https://www.nblog09.com/w/2019/02/03/django-limit/)

- メール送信関連
  - [Django で Gmail を送信する](https://qiita.com/ekzemplaro/items/3265f755eb4537b18478)

- ファイルアップロード関連
  - [[Django] ファイルアップロード機能の使い方 [基本設定編]](https://qiita.com/okoppe8/items/86776b8df566a4513e96)
  - [Python3 + google-api-python-clientで、Google Drive APIを使ってpdfファイルをアップロードし、OCR処理をする](https://thinkami.hatenablog.com/entry/2018/04/01/173611)
  - [「Google Drive REST API v3」に「アクセストークン」を付与してファイルを検索／ダウンロードする](https://qiita.com/CUTBOSS/items/2ccb543f68f1a6c1aa7d)
  - [JavaScript でファイル保存・開くダイアログを出して読み書きするまとめ](https://qiita.com/kerupani129/items/99fd7a768538fcd33420)
  - [Drive API Python Quickstart](https://developers.google.com/drive/api/v3/quickstart/python?hl=ja)
  - [Drive API Python Document](https://developers.google.com/resources/api-libraries/documentation/drive/v3/python/latest/drive_v3.files.html)
  - [Google Driveにpythonでデータを登録する & Siderを使ってチェックしてみる](https://qiita.com/akiko-pusu/items/f05a5dcba544e97c057c)
  - [How to fix “403 insufficient authentication scopes” when uploading file ](https://stackoverflow.com/questions/56099575/how-to-fix-403-insufficient-authentication-scopes-when-uploading-file-python)
  - [Drive API Scope](https://developers.google.com/drive/api/v3/about-auth)

- セキュリティ関連
  - [Django でランダムな文字列を生成するメモ](https://cortyuming.hateblo.jp/entry/20140529/p1)
  - [Djangoのセキュリティとその実装](https://www.slideshare.net/mobile/aki33524/django-58472909)

- Logging関連
  - [django#logging](https://qiita.com/soup01/items/068b2f3e3fe83026e4b7)
  - [Django ログ出力のまとめ](https://qiita.com/okoppe8/items/3e8ab77c5801a7d21991)
  - [djangoのloggerの(最低限の)使い方](https://qiita.com/sakamossan/items/a98b949738028ad39a6b)

- 例外処理関連
  - [Djangoで、404ページを作る](https://torina.top/detail/262/)
  - [【Django】独自の403、404、500 エラーページを作成する](https://canon1ky.hatenablog.com/entry/2018/10/15/215038)
  - [python – Django – キャッチ例外](https://codeday.me/jp/qa/20190408/579296.html)

- 日付関連
  - [python 現在時刻取得](disclosure.edinet-fsa.go.jp)

- Util関連
  - [属性の有無チェック](https://www.python-izm.com/advanced/hasattr/)
  - [Pythonの UTC ⇔ JST、文字列(UTC) ⇒ JST の変換とかのメモ](https://qiita.com/yoppe/items/4260cf4ddde69287a632)
  - [プルダウンリスト（Select）とマルチセレクトボックス。初期化と値の受取など。／Django2.0＋Bootstrap4](https://arakan-pgm-ai.hatenablog.com/entry/2019/02/14/090000)
  - [Pythonで文字列・数値をゼロ埋め（ゼロパディング）](https://note.nkmk.me/python-zero-padding/)
  - [Djangoのテンプレートで、キーに変数を指定して辞書にアクセス](http://y0m0r.hateblo.jp/entry/20140424/1398354294)
  - [Djangoでデータをcsv形式でダウンロードする方法](https://intellectual-curiosity.tokyo/2019/06/07/django%E3%81%A7%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92csv%E5%BD%A2%E5%BC%8F%E3%81%A7%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/)

- デコレータ関連
  - [PythonのデコレータでAOPっぽいことをしました。](https://qiita.com/naokiur/items/671f9cfd6b2d683f3de4)
  - [Python デコレータ再入門　 ~デコレータは種類別に覚えよう~](https://qiita.com/macinjoke/items/1be6cf0f1f238b5ba01b)
  - [Pythonのデコレータについて](https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e)
 
- フィルタ関連
  - [Django、フィルタを作る](https://torina.top/detail/240/)

- アーキテクチャ関連
  - [Djangoプロジェクト構造のカスタマイズ（分割と構造化）](https://qiita.com/aion/items/ca375efac5b90deed382)
  - [Pythonでシングルトン(Singleton)を実装してみる](http://www.denzow.me/entry/2018/01/28/171416)
  - [Python で定数を定義する](https://maku77.github.io/python/syntax/const.html)
  - [Python でシングルトンパターンを実装する](https://blog.bitmeister.jp/?p=4806)
  
- マイグレーション関連
  - [Table was deleted, how can I make Django recreate it?](https://stackoverflow.com/questions/33259477/table-was-deleted-how-can-i-make-django-recreate-it)

- UnitTest関連
  - [自動テストについてのまとめ](https://qiita.com/okoppe8/items/eb7c3be5b9f6be244549)

- デプロイ関連
  - [[Django] プロジェクト構成のベストプラクティスを探る - ２．設定ファイルを本番用と開発用に分割する](https://qiita.com/okoppe8/items/e60d35f55188c0ab9ecc)
  - [Heroku アプリに PostgreSQL を導入する](http://neos21.hatenablog.com/entry/2018/12/06/080000)
  - [Django session_data を定期的に削除する](https://www.monotalk.xyz/blog/django-session_data-%E3%82%92%E5%AE%9A%E6%9C%9F%E7%9A%84%E3%81%AB%E5%89%8A%E9%99%A4%E3%81%99%E3%82%8B/)
  - [HerokuのDjangoにSendGridを設定してメールを送る](https://www.mathpython.com/ja/sendgrid/)
  - [Herokuで消えるファイルと消えないファイル](http://uni8inu.hatenablog.com/entry/2016/12/08/000358)
 
- visual studio code 関連
  - [VS CodeでPythonの中間ファイル(.pyc)を非表示にする](https://www.sukerou.com/2019/03/vs-codepythonpyc.html)
  - [VS Code コーディング規約を快適に守る](https://qiita.com/firedfly/items/00c34018581c6cec9b84)
  - [VSCodeの設定画面(JSON)を表示させるショートカットの設定](https://qiita.com/Naturalclar/items/4682ff7c8deb8d8dfcff)
  
- macで開発する時の小ネタ
  - [Macにおけるバックスラッシュ（\）の入力方法](https://qiita.com/miyohide/items/6cb8967282d4b2db0f61)
  - [WindowsユーザーがMacに乗り換えた時に理解しておくとよい情報](https://qiita.com/yuusuke510/items/11cc201c6a2aa8bb42a8)

- 気が向いたらReact x Djangoする用のメモ
  - [DjangoのページをReactで作る - Webpack4](https://qiita.com/sand/items/15da91117c680a618c2b)
  - [Django+Reactで初めてのSPA作ったった](https://qiita.com/Mujica/items/e2c85a93e10ab931c6f7)
  - [React + Django REST FrameworkでToDoアプリを作りました](https://www.arimakaoru.com/blog/create-todoapp-react-django-rest-framework)
