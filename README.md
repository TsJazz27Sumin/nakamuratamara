Nakamuratamara
====

## Overview / 概要

- This web application made for a close university professor. To sharing reports with one's fellow students.
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

In Japan of recent date, Security incidents are occurring. Some cases, There was a leak of id and password. For example Home file service. So I design authentication feature without id and password.

Everytime administrator request onetime loginurl with his or her email input. Then email includes onetime loginurl is sent by Sendgrid API.

最近の日本では、セキュリティ事故が起きています。いくつかのケースでは、IDとパスワードが漏れています。そういった諸々もあって、IDとパスワードを使わない認証処理を設計しました。

常に管理者は、メールアドレスを入力してもらって一時的なログインURLを要求してもらいます。すると、一時的なログインURLが含まれたメールがSendgrid APIを利用して送信されます。

>Report file management.

Nowadays we can choose storage. AWS, Azure, GCP. But that costs money. Even if insignificant. So I design report file management with Google Drive API.

Report files are uploaded to individual google drive. For example, mine or professor storage.

今日では、私たちはAWSやAzure, GCPといったサービスのストレージを選択することが出来ます。しかし、微々たるものとはいえ、お金がかかります。そのためGoogle Drive APIを使ったレポートファイル管理を設計しました。

レポートファイルは、個人のGoogleドライブにアップロードされます。例えば、私や教授のGoogleドライブにです。

### Architecture / アーキテクチャ
 - Layerd Architecture x CQRS like I usually do. I am usually developing web applications with Java or C#.
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

[DJANGO-TIPS](https://github.com/TsJazz27Sumin/technical-tips/blob/master/DJANGO-TIPS.md)
