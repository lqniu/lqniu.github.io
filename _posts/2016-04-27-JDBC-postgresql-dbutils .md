---
layout: post
title: "JDBC连接postgresql数据库"
date:   2016-04-27 10:14:53
categories: study, database
---

1 裸连
String sql = "select * from test";

// 连接字符串，格式： "jdbc:数据库驱动名称://数据库服务器ip/数据库名称"
String url = "jdbc:postgresql://localhost/soft";
String username = "scott";
String password = "tiger";

Class.forName(""org.postgresql.Driver").newInstance();

Connection conn = DriverManager.getConnection(url, username, password); 
Statement  stmt = conn.createStatement(ResultSet.TYPE_SCROLL_SENSITIVE
                                     , ResultSet.CONCUR_UPDATABLE);
ResultSet  rs   = stmt.executeQuery(sql);

rs.close();
stmt.close();
conn.close();


2 使用dbutils
TestDB.java
public class TestDB {
  //初始化数据源
	private  static DataSource initDatasource(){
		BasicDataSource dataSource = new BasicDataSource();
		dataSource.setDriverClassName("org.postgresql.Driver");
		dataSource.setUsername("postgres");
		dataSource.setPassword("111111");
		dataSource.setUrl("jdbc:postgresql://localhost/postgres");
		return dataSource;
	}
	//利用Queryrunner进行插入操作
	public Object insert(String sql, Object param[]) throws SQLException{
		DataSource dataSource = initDatasource();
		QueryRunner queryRunner = new QueryRunner(dataSource);
		return queryRunner.update(sql, param);
	}
	//利用Queryrunner进行查询操作
	public List<City> queryList(String sql, Object[] param, Class class1) throws SQLException{
		DataSource dataSource = initDatasource();
		QueryRunner queryRunner = new QueryRunner(dataSource);
		List<City> list = (List<City>) queryRunner.query(sql, new BeanListHandler<City>(class1),param);
		return list;
	} 
	@SuppressWarnings("restriction")
	public static void main(String[] args) throws SQLException {
		// TODO Auto-generated method stub
		TestDB testDB = new TestDB();
		//简单的ORM，可以将查询结果转换为City类
		List<City> list = testDB.queryList("select * from City ", null, City.class);
		for (Iterator iterator = list.iterator(); iterator.hasNext();) {
			City city = (City) iterator.next();
			System.out.println(city);
		}
	}
}

City.java
public class City {
	private int city_id;
	private String city;
	private int counttry_id;
	private Date last_update;
	public int getCity_id() {
		return city_id;
	}
	public void setCity_id(int city_id) {
		this.city_id = city_id;
	}
	public String getCity() {
		return city;
	}
	public void setCity(String city) {
		this.city = city;
	}
	public int getCounttry_id() {
		return counttry_id;
	}
	public void setCounttry_id(int counttry_id) {
		this.counttry_id = counttry_id;
	}
	public Date getLast_update() {
		return last_update;
	}
	public void setLast_update(Date last_update) {
		this.last_update = last_update;
	}
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		//利用ToStringBuilder可以方便的为自定义的类生成toString方法,JSON_STYLE相当于直接转换为json字符串
		//ref http://commons.apache.org/proper/commons-lang/apidocs/org/apache/commons/lang3/builder/ToStringStyle.html
		return ToStringBuilder.reflectionToString(this, ToStringStyle.JSON_STYLE);
	}
}
