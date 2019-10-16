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
-- Name: body_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.body_type (
    id integer NOT NULL,
    "body type" character varying(200) NOT NULL
);


ALTER TABLE public.body_type OWNER TO postgres;

--
-- Name: body_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.body_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.body_type_id_seq OWNER TO postgres;

--
-- Name: body_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.body_type_id_seq OWNED BY public.body_type.id;


--
-- Name: engine; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.engine (
    id integer NOT NULL,
    engine character varying(200) NOT NULL
);


ALTER TABLE public.engine OWNER TO postgres;

--
-- Name: engine_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.engine_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.engine_id_seq OWNER TO postgres;

--
-- Name: engine_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.engine_id_seq OWNED BY public.engine.id;


--
-- Name: manufacturersize; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.manufacturersize (
    id integer NOT NULL,
    manufacturersize character varying(200) NOT NULL,
    country character varying(200) NOT NULL,
    email character varying(200) NOT NULL
);


ALTER TABLE public.manufacturersize OWNER TO postgres;

--
-- Name: manufacturersize_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.manufacturersize_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.manufacturersize_id_seq OWNER TO postgres;

--
-- Name: manufacturersize_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.manufacturersize_id_seq OWNED BY public.manufacturersize.id;


--
-- Name: models; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.models (
    id integer NOT NULL,
    year integer NOT NULL,
    model character varying(200) NOT NULL,
    model_size integer NOT NULL,
    body_type integer NOT NULL,
    engenie integer NOT NULL,
    idm integer
);


ALTER TABLE public.models OWNER TO postgres;

--
-- Name: models_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.models_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.models_id_seq OWNER TO postgres;

--
-- Name: models_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.models_id_seq OWNED BY public.models.id;


--
-- Name: size; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.size (
    id integer NOT NULL,
    size character varying(200) NOT NULL
);


ALTER TABLE public.size OWNER TO postgres;

--
-- Name: size_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.size_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.size_id_seq OWNER TO postgres;

--
-- Name: size_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.size_id_seq OWNED BY public.size.id;


--
-- Name: body_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.body_type ALTER COLUMN id SET DEFAULT nextval('public.body_type_id_seq'::regclass);


--
-- Name: engine id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.engine ALTER COLUMN id SET DEFAULT nextval('public.engine_id_seq'::regclass);


--
-- Name: manufacturersize id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manufacturersize ALTER COLUMN id SET DEFAULT nextval('public.manufacturersize_id_seq'::regclass);


--
-- Name: models id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.models ALTER COLUMN id SET DEFAULT nextval('public.models_id_seq'::regclass);


--
-- Name: size id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.size ALTER COLUMN id SET DEFAULT nextval('public.size_id_seq'::regclass);


--
-- Data for Name: body_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.body_type (id, "body type") FROM stdin;
1	Convertible
2	Coupe
3	Crossover
4	Green Car or Hybrid
5	Luxury Car
6	Minivan or Van
7	Pickup Truck
8	SUV
9	Sedan
10	Sports Car
11	Wagon or Hatchback
\.


--
-- Data for Name: engine; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.engine (id, engine) FROM stdin;
1	gasoline
2	diesel
3	electro
4	hydrogen
5	hybrid
\.


--
-- Data for Name: manufacturersize; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.manufacturersize (id, manufacturersize, country, email) FROM stdin;
1	Acura	Japan	www.acura.me
2	Alfa Romeo	Italy	www.alfaromeo.com
3	Aston Martin	United Kingdom	www.astonmartin.com
4	Audi	Germany	www.audi.com
5	Bentley	United Kingdom	www.bentleymotors.com
6	BMW	Germany	www.bmwgroup.com
7	Buick	USA	www.buick.com
8	Cadillac	USA	www.cadillac.com
9	Chevrolet	USA	www.chevrolet.com
10	Chrysler	USA	www.fcagroup.com
11	Dodge	USA	www.dodge.com
12	Ferrari	Italy	www.ferrari.com
13	FIAT	Italy	www.fiat.com
14	Ford	USA	www.ford.com
15	Genesis	South Korea	www.genesis.com
16	GMC	USA	www.gmc.com
17	Honda	Japan	global.honda
18	Hyundai	South Korea	www.hyundaimotorgroup.com
19	INFINITI	Japan	www.infiniti.com
20	Jaguar	United Kingdom	www.jaguar.com
21	Jeep	USA	www.jeep.com
22	Kia	South Korea	www.kia.com
23	Lamborghini	Italy	www.lamborghini.com
24	Land Rover	United Kingdom	www.landrover.com
25	Lexus	Japan	discoverlexus.com
26	Lincoln	USA	www.lincoln.com
27	Lotus	United Kingdom	www.lotuscars.com
28	Maserati	Italy	www.maserati.com
29	Mazda	Japan	www.mazda.com
30	McLaren	United Kingdom	www.mclaren.com
31	Mercedes-Benz	Germany	www.mercedes-benz.com
32	MINI	United Kingdom	www.mini.com
33	Mitsubishi	Japan	www.mitsubishi-motors.com
34	Nissan	Japan	www.nissan-global.com
35	Porsche	Germany	www.porsche.com
36	RAM	United Kingdom	www.ramracing.com
37	Rolls-Royce	United Kingdom	www.rolls-roycemotorcars.com
38	smart	Germany	www.smart.com
39	Subaru	Japan	www.subaru-global.com
40	Tesla	USA	www.tesla.com
41	Toyota	Japan	global.toyota
42	Volkswagen	Germany	volkswagen.com
43	Volvo	Swedish	www.volvogroup.com
\.


--
-- Data for Name: models; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.models (id, year, model, model_size, body_type, engenie, idm) FROM stdin;
75	2011	Lincoln Navigator	3	8	1	26
76	2019	Lincoln MKZ Hybrid	2	9	1	26
77	2017	Lincoln MKC	1	8	1	26
1	2019	Acura ILX	1	9	1	1
2	2020	Acura MDX Sport Hybrid	2	8	5	1
3	2019	Acura NSX	2	10	5	1
4	2018	Alfa Romeo 4C Spider	1	10	1	2
5	2019	Alfa Romeo Giulia	2	9	1	2
6	2019	Alfa Romeo Stelvio	1	8	1	2
7	2017	Aston Martin V12 Vantage S	1	10	1	3
8	2018	Aston Martin DB11	1	2	1	3
9	2018	Aston Martin Vanquish	1	2	1	3
10	2018	Audi A8	3	5	1	4
11	2018	Audi Q7	3	8	2	4
12	2018	Audi R8	3	2	1	4
13	2019	Bentley Mulsanne	3	9	1	5
14	2018	Bentley Continental GT	2	1	1	5
78	2018	Lotus Evora 400	1	10	1	27
79	2011	Lotus Exige	1	10	1	27
80	2008	Lotus Elise	1	10	1	27
15	2017	BMW 330	1	9	1	6
16	2018	BMW 330 Gran Turismo	2	11	2	6
17	2018	BMW 750	3	9	1	6
18	2019	Buick Cascada	1	1	1	7
19	2018	Buick Regal TourX	2	11	2	7
20	2017	Buick Enclave	3	8	2	7
21	2018	Cadillac ATS-V	1	10	1	8
22	2019	Cadillac CTS	2	5	1	8
23	2019	Cadillac Escalade ESV	3	8	5	8
24	2019	Chevrolet Silverado 2500	4	7	1	9
25	2019	Chevrolet Bolt EV	1	11	3	9
26	2017	Chevrolet Express 2500	4	6	2	9
27	2017	Chrysler Pacifica Hybrid	2	6	4	10
28	2017	Chrysler 300C	3	8	1	10
29	2017	Chrysler 200	2	9	1	10
30	2017	Dodge Challenger	2	2	1	11
31	2017	Dodge Charger	3	9	1	11
32	2017	Dodge Durango	3	8	1	11
33	2017	Ferrari California	1	1	1	12
34	2018	Ferrari 812 Superfast	1	10	1	12
35	2018	Ferrari 488 GTB	1	2	1	12
36	2017	FIAT 500	1	11	1	13
37	2017	FIAT 124 Spider	1	10	1	13
38	2017	FIAT 500X	1	8	1	13
39	2017	Ford F-450	4	7	2	14
40	2019	Ford Mustang	1	10	1	14
41	2019	Ford Focus Electric	2	9	3	14
42	2017	Genesis G90	3	9	1	15
43	2018	Genesis G80	2	9	1	15
44	2019	Genesis G70	1	9	1	15
45	2017	GMC Savana 2500	4	6	2	16
46	2017	GMC Yukon XL	4	8	1	16
47	2018	GMC Sierra 3500	4	7	2	16
49	2019	Honda Clarity Plug-In Hybrid	2	9	5	17
48	2018	Honda Civic Type R	1	10	1	17
50	2017	Honda Pilot	3	8	1	17
51	2018	Hyundai Santa Fe	3	8	1	18
52	2017	Hyundai Sonata Hybrid	2	9	5	18
53	2019	Hyundai Veloster	1	11	1	18
54	2018	INFINITI QX80	3	5	1	19
55	2018	INFINITI Q70h	2	9	5	19
56	2018	INFINITI Q60	1	2	1	19
57	2017	Jaguar XJ	3	9	1	20
58	2018	Jaguar XF	2	9	5	20
59	2020	2020 Jaguar F-TYPE	1	10	1	20
60	2017	Jeep Grand Cherokee	2	8	1	21
61	2017	Jeep New Compass	1	8	1	21
62	2020	Jeep Gladiator	1	7	1	21
63	2017	Kia K900	3	5	1	22
64	2017	Kia Stinger	2	9	1	22
65	2019	Kia Soul EV	1	11	3	22
66	2018	Lamborghini Aventador S	2	2	1	23
67	2019	Lamborghini Urus	2	8	1	23
68	2017	Lamborghini Aventador	2	10	1	23
69	2019	Land Rover Range Rover Velar	3	8	2	24
70	2017	Land Rover Range Rover Evoque	1	8	1	24
71	2019	Land Rover Range Rover Sport	2	8	2	24
72	2018	Lexus LS 500h	3	9	5	25
73	2017	Lexus RC F	2	10	1	25
74	2017	Lexus CT 200h	1	11	5	25
81	2010	Maserati GranTurismo Convertible	2	10	1	28
83	2019	Maserati Levante Trofeo	2	8	1	28
84	2019	Mazda СХ-9	3	8	1	29
86	2017	Mazda MX-5 Miata	1	10	1	29
85	2018	Mazda 6	2	9	1	29
82	2014	Maserati Quattroporte	3	9	1	28
87	2017	McLaren 570GT	1	10	1	30
88	2019	McLaren 570GT	1	10	1	30
89	2018	McLaren 570S Spider	1	10	1	30
90	2020	Mercedes-AMG ONE	1	10	1	31
91	2018	Mercedes-AMG GLS 63	3	8	1	31
92	2019	Mercedes-Benz CLS-Class	2	9	1	31
93	2016	MINI John Cooper Works Hardtop	2	11	1	32
94	2013	MINI Cooper Convertible	1	1	1	32
95	2018	MINI Cooper Countryman Plug-in Hybrid	2	8	5	32
96	2018	Mitsubishi Mirage	1	11	1	33
97	2020	Mitsubishi Outlander PHEV	2	8	5	33
98	2015	Mitsubishi Lancer Evolution	2	9	1	33
99	2018	Nissan 370Z Nismo	1	2	1	34
100	2010	Nissan Titan	4	7	1	34
101	2019	Nissan GT-R NISMO	2	10	1	34
\.


--
-- Data for Name: size; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.size (id, size) FROM stdin;
1	Compact
2	Midsize
3	Full-Size
4	Heavy-Duty - Pickups
\.


--
-- Name: body_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.body_type_id_seq', 11, true);


--
-- Name: engine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.engine_id_seq', 5, true);


--
-- Name: manufacturersize_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.manufacturersize_id_seq', 43, true);


--
-- Name: models_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.models_id_seq', 101, true);


--
-- Name: size_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.size_id_seq', 4, true);


--
-- Name: body_type body_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.body_type
    ADD CONSTRAINT body_type_pkey PRIMARY KEY (id);


--
-- Name: engine engine_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.engine
    ADD CONSTRAINT engine_pkey PRIMARY KEY (id);


--
-- Name: manufacturersize manufacturersize_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manufacturersize
    ADD CONSTRAINT manufacturersize_pkey PRIMARY KEY (id);


--
-- Name: models models_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.models
    ADD CONSTRAINT models_pkey PRIMARY KEY (id);


--
-- Name: size size_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.size
    ADD CONSTRAINT size_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

