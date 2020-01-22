SET ECHO OFF
SET SQLBLANKLINES ON
--SET HEADING OFF
SET LINESIZE 1000
SET PAGESIZE 9999
SET TERM OFF
SET FEED OFF
SET VERIFY OFF
SET TRIMSPOOL ON

spool &&patch
--spool _Result\ChecksResult.txt

column isErr		format a30
column n			format 9999
column rule_cd		format a20
column create_ts	format date

prompt [DQ_RULE]
select distinct isErr
	, n
	, rule_cd
	, create_ts
from table1
where agrmnt_claim in (&1)
order by n;
