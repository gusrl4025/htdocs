#positional formating
print('to {}. Thanks to the flexibility of Python and the powerful ecosystem of packages, {} the Azure CLI supports features such as autocompletion (in shells that support it), persistent credentials, JMESPath result parsing, lazy initialization, {} network-less unit tests, and more.'.format('apple',12,'apple'))

#Named placeholder
print('to {name:s}. Thanks to the flexibility of Python and the powerful ecosystem of packages, {age:d} the Azure CLI supports features such as autocompletion (in shells that support it), persistent credentials, JMESPath result parsing, lazy initialization, {name} network-less unit tests, and more.'.format(name='apple',age=12))