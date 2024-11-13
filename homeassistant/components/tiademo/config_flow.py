"""Config flow for TIA DEMO integration."""

from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigFlow

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class ConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for TIA DEMO."""

    VERSION = 1
    _LOGGER.debug("ConfigFlow")
