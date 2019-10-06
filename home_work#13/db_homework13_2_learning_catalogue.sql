--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5 (Ubuntu 11.5-0ubuntu0.19.04.1)
-- Dumped by pg_dump version 11.5 (Ubuntu 11.5-0ubuntu0.19.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: courses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.courses (
    c_no text NOT NULL,
    title text,
    hours integer
);


ALTER TABLE public.courses OWNER TO postgres;

--
-- Name: exams; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.exams (
    s_id integer NOT NULL,
    c_no text NOT NULL,
    score integer
);


ALTER TABLE public.exams OWNER TO postgres;

--
-- Name: groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.groups (
    g_no text NOT NULL,
    monitor integer NOT NULL
);


ALTER TABLE public.groups OWNER TO postgres;

--
-- Name: students; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.students (
    s_id integer NOT NULL,
    name text,
    start_year integer,
    g_no text
);


ALTER TABLE public.students OWNER TO postgres;

--
-- Data for Name: courses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.courses (c_no, title, hours) FROM stdin;
CS305	Сети ЭВМ	60
CS301	Базы данных	60
\.


--
-- Data for Name: exams; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.exams (s_id, c_no, score) FROM stdin;
1451	CS301	5
1556	CS301	5
1451	CS305	5
\.


--
-- Data for Name: groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.groups (g_no, monitor) FROM stdin;
A-101	1451
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.students (s_id, name, start_year, g_no) FROM stdin;
1451	Анна	2014	\N
1432	Виктор	2014	\N
1556	Нина	2015	\N
\.


--
-- Name: courses courses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_pkey PRIMARY KEY (c_no);


--
-- Name: groups groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (g_no);


--
-- Name: exams pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exams
    ADD CONSTRAINT pk PRIMARY KEY (s_id, c_no);


--
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (s_id);


--
-- Name: exams exams_c_no_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exams
    ADD CONSTRAINT exams_c_no_fkey FOREIGN KEY (c_no) REFERENCES public.courses(c_no);


--
-- Name: exams exams_s_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.exams
    ADD CONSTRAINT exams_s_id_fkey FOREIGN KEY (s_id) REFERENCES public.students(s_id);


--
-- Name: groups groups_monitor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_monitor_fkey FOREIGN KEY (monitor) REFERENCES public.students(s_id);


--
-- Name: students students_g_no_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_g_no_fkey FOREIGN KEY (g_no) REFERENCES public.groups(g_no);


--
-- PostgreSQL database dump complete
--

