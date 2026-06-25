# Development Log

## 2026-08-22

### Gjort
- Ryddet prosjektstruktur.
- Flyttet simulering til funksjoner.
- main gjør alle funskjonskall.
- Implementerte RK4.

### Observasjoner
- RK4 virker betydelig mer nøyaktig enn Euler.
- Forskjellen blir større når dt økes.
- RK4 er dyrere per steg fordi modellen evalueres fire ganger. Men presisjonen dens gjør opp for dette med mere. 

