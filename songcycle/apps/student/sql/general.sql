--SELECT
select * from public.student_accessinformation;

--mygrationをやり直したいときに使う。
delete from public.django_migrations where app = 'student';
drop table public.student_applicationuser;
drop table public.student_accessinformation;
drop table public.student_masterdata;

--UserSample
insert into public.student_applicationuser(id, email, first_name, last_name, authority, active, first_login_date_timestamp, last_login_date_timestamp, login_count, comment) values (1, 'xxx', '', '', '00101', '01', current_timestamp, current_timestamp, 0, 'comment');
insert into public.student_applicationuser(id, email, first_name, last_name, authority, active, first_login_date_timestamp, last_login_date_timestamp, login_count, comment) values (2, 'test2@test.com', '', '', '00102', '01', current_timestamp, current_timestamp, 0, 'comment');
insert into public.student_applicationuser(id, email, first_name, last_name, authority, active, first_login_date_timestamp, last_login_date_timestamp, login_count, comment) values (3, 'test3@test.com', '', '', '00102', '02', current_timestamp, current_timestamp, 0, 'comment');
