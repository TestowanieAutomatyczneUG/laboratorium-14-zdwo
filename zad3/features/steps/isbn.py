from behave import *
from src.sample.isbn import ISBN

@given("Algorithm")
def step_impl(context):
    context.isbn = ISBN()


@when('{number}')
def step_impl(context, number):
    context.result = context.isbn.alg(number)


@then('{result}')
def step_impl(context, result):
    assert context.result == int(result)




