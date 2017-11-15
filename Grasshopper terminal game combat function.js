function combat(health, damage) {
  var newHealth = health - damage;
    if (newHealth < 0) {
      return 0;
  }
  return newHealth;
}
