def dekorator_funksiyasi(original_funksiya):
    def qadoqlovchi_funksiyasi(*args, **kwargs):
        print(f"{original_funksiya.__name__} funksiyasi chaqirilishidan oldin.")
        natija = original_funksiya(*args, **kwargs)
        print(f"{original_funksiya.__name__} funksiyasi chaqirilgandan keyin.")
        return natija
    return qadoqlovchi_funksiyasi

@dekorator_funksiyasi
def salomlash():
    print("Salom!")

salomlash()