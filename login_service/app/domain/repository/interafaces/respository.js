class RepositoryInterface {
    constructor() {
        if(!this.getUser) {
            console.log("must have getUser!");
        }
        if(!this.saveUser) {
            console.log("must have saveUser!");
        }
    }
}
module.exports = RepositoryInterface