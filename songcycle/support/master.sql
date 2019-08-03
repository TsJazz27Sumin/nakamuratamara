truncate table public.student_applicationuser;

insert into public.student_applicationuser(id, user_id, email, first_name, last_name, full_name, authority, active, first_login_date_timestamp, last_login_date_timestamp, login_count, comment, create_user_id, create_timestamp, update_user_id, update_timestamp) values (nextval('student_applicationuser_id_seq'::regclass), 'U0001', 'test1@example.com', 'test', '001', 'test001' ,'01', '01', current_timestamp, current_timestamp, 0, 'comment', 'U0001',current_timestamp, 'U0001',current_timestamp);
insert into public.student_applicationuser(id, user_id, email, first_name, last_name, full_name, authority, active, first_login_date_timestamp, last_login_date_timestamp, login_count, comment, create_user_id, create_timestamp, update_user_id, update_timestamp) values (nextval('student_applicationuser_id_seq'::regclass), 'U0002', 'test2@example.com', 'test', '002', 'test002' ,'02', '01', current_timestamp, current_timestamp, 0, 'comment', 'U0001',current_timestamp, 'U0001',current_timestamp);
insert into public.student_applicationuser(id, user_id, email, first_name, last_name, full_name, authority, active, first_login_date_timestamp, last_login_date_timestamp, login_count, comment, create_user_id, create_timestamp, update_user_id, update_timestamp) values (nextval('student_applicationuser_id_seq'::regclass), 'U0003', 'test3@example.com', 'test', '003', 'test003' ,'02', '02', current_timestamp, current_timestamp, 0, 'comment', 'U0001',current_timestamp, 'U0001',current_timestamp);

truncate table public.student_masterdata;

insert into public.student_masterdata(
	id, code, sub_code, value, sub_value, comment)
values (nextval('student_masterdata_id_seq'::regclass),
     '001', '01', 'admin', '', 'ユーザー権限：管理者');

insert into public.student_masterdata(
	id, code, sub_code, value, sub_value, comment)
values (nextval('student_masterdata_id_seq'::regclass),
     '001', '02', 'student', '', 'ユーザー権限：学生');

insert into public.student_masterdata(
	id, code, sub_code, value, sub_value, comment)
values (nextval('student_masterdata_id_seq'::regclass),
     '002', '01', 'active', '', 'ユーザー状態：有効');

insert into public.student_masterdata(
	id, code, sub_code, value, sub_value, comment)
values (nextval('student_masterdata_id_seq'::regclass),
     '002', '02', 'sleep', '', 'ユーザー権限：休眠');

insert into public.student_masterdata(
	id, code, sub_code, value, sub_value, comment)
values (nextval('student_masterdata_id_seq'::regclass),
     '003', '01', '15', '', 'テンポラリーログインURLの有効期間');

insert into public.student_masterdata(
	id, code, sub_code, value, sub_value, comment)
values (nextval('student_masterdata_id_seq'::regclass),
     '004', '01', 'http://127.0.0.1:8000/student/login/?onetimepassword=', '', 'テンポラリーログインURLのルート');

insert into public.student_masterdata(
	id, code, sub_code, value, sub_value, comment)
values (nextval('student_masterdata_id_seq'::regclass),
     '005', '01', 'request_login', '', 'event_type');

truncate table public.student_numberingmaster;

insert into public.student_numberingmaster(
	id, code, initial, value, comment)
	values (1, '01', 'U', 3, 'User Id');

insert into public.student_numberingmaster(
	id, code, initial, value, comment)
	values (2, '02', 'R', 0, 'Report Id');

insert into public.student_numberingmaster(
	id, code, initial, value, comment)
	values (3, '03', 'D', 0, 'Download Id');