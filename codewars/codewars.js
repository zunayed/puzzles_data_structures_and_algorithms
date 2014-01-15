exports.solution = function(nums){
  return (nums || []).sort(function(a, b){
    return a - b    
  });
}

exports.nameSpace = function(){
	var MyNamespace = MyNamespace || {};

	this.MyNamespace.MyClass = function(phrase){
	  this.phrase = phrase;
	};

	return MyNamespace;
}