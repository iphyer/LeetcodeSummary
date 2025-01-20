interface String {
    replicate(times: number): string;
}

/*
String.prototype.replicate = function(times): string {
    if (times === 0) {
        return "";
    }
    //Here "this" refers to the string object on which the method is called
    return this + this.replicate(times - 1);
}
*/

String.prototype.replicate = function(times: number) {
    let result = "";
    for (let i = 0; i < times; i++) {
        result += this;
    }
    return result;
};
