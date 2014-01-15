var assert = require('assert');
var codewars = require('../codewars');
 

var MyNamespace = MyNamespace || {};

MyNamespace.MyClass = function(phrase){
  this.phrase = phrase;
};


describe('codewars tests', function(){

    // it('should sort an array of numbers', function() {
    //   assert.equal(codewars.solution([1,3,2,5,4]), [1,2,3,4,5]);

    // }); 

    it("should define a class, MyClass, in the namespace MyNamespace", function () {
    	assert.equal(typeof MyNamespace.MyClass == 'function', true);
    });

    it("should define a class, MyClass, in the namespace MyNamespace", function () {

		var MyNamespace = codewars.nameSpace;
		console.log(typeof MyNamespace.MyClass)
    	assert.equal(typeof MyNamespace.MyClass == 'function', true);
    });
});

// describe("A Namespaced Object", function () {
  
//   it("should define a class, MyClass, in the namespace MyNamespace", function () {
//     Test.expect(typeof MyNamespace.MyClass == 'function');

//     var myclass = new MyNamespace.MyClass();
//     Test.expect(typeof myclass == 'object');
//   });
  
//   it("should not expose MyClass globally", function () {
//     Test.expect(typeof MyClass == 'undefined');
//     Test.expect(typeof sayHello == 'undefined');
//   });
  
//   it("should not overwrite existing objects in the namespace", function () {
//     Test.expect(MyNamespace.TestClass);
//     Test.expect((new MyNamespace.TestClass2()).blue == 'green');
//   });
  
//   it("should define a method in MyClass that returns 'hello'", function () {
//     var obj = new MyNamespace.MyClass('hello');
//     Test.expect(obj.sayHello() == 'hello');
//   });
  
//   it("should not replace the existing namespace object", function () {
//     Test.expect(OtherNamespace === MyNamespace);
//   });
// });