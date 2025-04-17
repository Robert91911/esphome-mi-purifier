#include "mi_purifier.h"
#include "esphome/core/log.h"

namespace esphome
{
  namespace mi_purifier
  {

    static const char *const TAG = "mi_purifier";

    void MiPurifier::setup()
    {
      ESP_LOGI(TAG, "Setting up MiPurifier...");
      // inicialización aquí
    }

    void MiPurifier::loop()
    {
      // lógica de lectura periódica
    }

  } // namespace mi_purifier
} // namespace esphome
