--SELECT
select * from public.student_accessinformation;

--mygrationをやり直したいときに使う。
delete from public.django_migrations where app = 'student';
delete from public.django_content_type where app_label = 'student';
drop table public.student_applicationuser;
drop table public.student_accessinformation;
drop table public.student_temporarilyloginurl;
drop table public.student_masterdata;
drop table public.student_report;
drop table public.student_downloadinformation;
drop table public.student_numberingmaster;