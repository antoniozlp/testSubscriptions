

createDatum = '''
mutation($value:Float, $code:String){
  createDatum(
    value:$value
    variableCode:$code
  )
  {
    successful
    messages{message}
  }
}'''

updateVariableState = '''mutation($endAt:DateTime, $id:ID!){
  updateVariableState(
    id:$id
    variableState:{endAt:$endAt}
  )
  {
    successful
    messages{message}
  }
}'''

createVariableState = '''mutation($variableCode:String, $startAt:DateTime, $state:State){
  createVariableState(
    state:$state
    variableCode: $variableCode #"Core_Temperature"
    startAt: $startAt #"2020-06-18T23:43:24Z"
  )
  {
    successful
    messages{message, field}
    result{id}
  }
}'''

variableStates = '''
query($variableCode:String){
  variableStates(filter:{variableCode:$variableCode} orderBy:{desc:ID} limit:1){
    id
    variable{code}
    state
    startAt
    endAt
  }
}'''