
select 
  models.id, models.year, models.model, s1.size as size_body, b1."body type",
  e1.engine, m1.manufacturersize, m1.country, m1.email
  from models inner join size as s1 on (models.model_size = s1.id)
  inner join body_type as b1 on (models.body_type = b1.id)
  inner join engine as e1 on (models.engenie = e1.id)
  inner join manufacturersize as m1 on (m1.id = models.idm) order by 1;

select 
  models.id, models.year, models.model, s1.size as size_body, b1."body type",
  e1.engine, m1.manufacturersize, m1.country, m1.email
  from models inner join size as s1 on (models.model_size = s1.id)
  inner join body_type as b1 on (models.body_type = b1.id)
  inner join engine as e1 on (models.engenie = e1.id)
  inner join manufacturersize as m1 on (m1.id = models.idm and m1.country = "USA") order by 1;

select 
  models.id, models.year, models.model, s1.size as size_body, b1."body type",
  e1.engine, m1.manufacturersize, m1.country, m1.email
  from models inner join size as s1 on (models.model_size = s1.id)
  inner join body_type as b1 on (models.body_type = b1.id)
  inner join engine as e1 on (models.engenie = e1.id and e1.engine = 'electro')
  inner join manufacturersize as m1 on (m1.id = models.idm) order by 1;

select
  models.id, models.year, models.model, s1.size as size_body, b1."body type",
  e1.engine, m1.manufacturersize, m1.country, m1.email
  from models inner join size as s1 on (models.model_size = s1.id )
  inner join body_type as b1 on (models.body_type = b1.id and b1."body type"= 'Sports Car')
  inner join engine as e1 on (models.engenie = e1.id )
  inner join manufacturersize as m1 on (m1.id = models.idm) order by 1;