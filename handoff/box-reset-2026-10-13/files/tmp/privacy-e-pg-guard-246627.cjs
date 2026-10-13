const Module = require('module');
const load = Module._load;
Module._load = function(request, parent, isMain) {
  if (request === 'pg') throw new Error('pg-constructed');
  return load.apply(this, arguments);
};