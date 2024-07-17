# Todo tutorial
使用 APIFlask 建立 Restful API 的範例程式

### v0.1 
  - 運用 Factory Pattern 建立 Flask App

### v0.2 
  - 建立 domain model 'TodoItem'
  - 加入 api blueprint 'todo_list_bp'
  - 加入 api  '/todo_list/all', return all todo items by user_id

### v0.3
  - 新增 ORM model of Todo
  - 修改 api '/todo_list/all' to access todos from DB

### v0.4
  - 新增 BaseOrmRepository (套用 singleton pattern)
  - 新增 TodoRepository (套用 repository pattern)
  - 修改 api '/todo_list/all' 改用 TodoRepository 來查詢資料

### v0.5
  - 新增 User Model, UserRepository 
  - 修改 Todo ORM model 加入 user_id 的 ForeignKey 資訊
  - 利用 flask_praetorian 套件來實作 JWT 認證機制
  - 在create_app() 利用 @app.teardown_appcontext 註用 shutdown_session(), 在其中 remove db_session
