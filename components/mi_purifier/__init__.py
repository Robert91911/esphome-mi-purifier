from esphome.components import uart
import esphome.codegen as cg

AUTO_LOAD = ['sensor']
DEPENDENCIES = ['uart']

mi_purifier_ns = cg.esphome_ns.namespace('mi_purifier')
MiPurifier = mi_purifier_ns.class_('MiPurifier', cg.Component, uart.UARTDevice)

CONFIG_SCHEMA = (
    cg.Schema({
        cg.GenerateID(): cg.declare_id(MiPurifier),
        cg.Required("uart_id"): cg.use_id(uart.UARTComponent),
    })
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
