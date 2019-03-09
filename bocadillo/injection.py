from aiodine import Store, scopes

# pylint: disable=invalid-name
_STORE = Store(
    scope_aliases={"request": scopes.FUNCTION, "app": scopes.SESSION},
    providers_module="providerconf",
    default_scope=scopes.FUNCTION,
)
provider = _STORE.provider
discover_providers = _STORE.discover
useprovider = _STORE.useprovider
create_context_provider = _STORE.create_context_provider
consumer = _STORE.consumer
freeze_providers = _STORE.freeze
