from pyknow import KnowledgeEngine, DefFacts

class RazonamientoNoMonotono(KnowledgeEngine):
    @DefFacts()
    def hechos_iniciales(self):
        yield Fact(nublado=True)
        yield Fact(lluvia=True)

    @Rule(OR(Fact(nublado=True), Fact(lluvia=True)))
    def conclusion(self):
        self.declare(Fact(buen_tiempo=False))

engine = RazonamientoNoMonotono()
engine.reset()
engine.run()

if not engine.facts["buen_tiempo"]:
    print("El tiempo no es bueno debido a la nubosidad o la lluvia.")
