const RepositoryInterface =  require('../domain/repository/interafaces/respository.js')
const User = require('../domain/repository/entities/users.js')
const mysql = require('mysql2');

class mysqlRepository extends RepositoryInterface {
    constructor() {
        super();
        this.connection = mysql.createConnection({
            host     : process.env.MYSQL_HOST,
            user     : 'root',
            password : 'test01',
            database : 'login'
        });
        this.connection.connect();
    }
    getUser(user) {
        return new Promise(async (resolve, reject) => {
        var error, results, fields = await this.connection.promise().query(`SELECT * FROM Users WHERE name = '${user.username}' AND password = '${user.password}';`)
        console.log(fields[0])
        console.log(fields[0].length)
        if (fields[0].length != 0){
            user = new User(fields[0][0]["id"], fields[0][0]["username"], fields[0][0]["password"], fields[0][0]["email"])
            resolve([false, user])
        }
        else {
            resolve([true, null])
        }
        })
    }
    async saveUser(user) {
        return new Promise(async (resolve, reject) => {
        var id = Math.floor(Math.random() * 9999)
        var error, results, fields = await this.connection.promise().query(`INSERT INTO Users ( id, name, password, email) VALUES( '${id}', '${user.username}', '${user.password}', '${user.email}');`) 
        // ON DUPLICATE KEY UPDATE name='${user.username}', password='${user.password}', email='${user.email}';`)
        console.log(fields)
        if (error) {
            return resolve([true, null])
        }
        else {
            return resolve([false, id])
        }
        })
    }
}

module.exports = mysqlRepository