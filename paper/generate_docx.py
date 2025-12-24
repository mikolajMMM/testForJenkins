from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from docx import Document
from docx.shared import Pt


@dataclass(frozen=True)
class Citation:
    n: int
    text: str


def _add_superscript_citation(paragraph, n: int) -> None:
    run = paragraph.add_run(str(n))
    run.font.superscript = True


def _add_paragraph_with_citations(
    doc: Document,
    text_parts: list[str],
    citations: list[int] | None = None,
) -> None:
    """
    text_parts: list of strings that are concatenated into one paragraph.
    citations: optional list of citation numbers appended at the end.
    """
    p = doc.add_paragraph("".join(text_parts))
    if citations:
        p.add_run(" ")
        for i, c in enumerate(citations):
            if i > 0:
                p.add_run(",")
            _add_superscript_citation(p, c)


def build_document() -> tuple[Document, list[Citation]]:
    """
    Creates a DOCX containing: Wstęp + Rozdział I + Rozdział II + przypisy końcowe.
    Footnotes are represented as superscripts and a final 'Przypisy' section.
    """
    citations: list[Citation] = [
        Citation(
            1,
            "Malta, Criminal Code (Chapter 9), consolidated text on Legislation Malta (ELI). "
            "Dostęp: 24.12.2025, https://legislation.mt/eli/cap/9/eng/html",
        ),
        Citation(
            2,
            "Netherlands, Wet afbreking zwangerschap (WAZ), consolidated text on "
            "wetten.overheid.nl (BWBR0003396). Dostęp: 24.12.2025, https://wetten.overheid.nl/BWBR0003396/",
        ),
        Citation(
            3,
            "BVerfG, Urteil des Zweiten Senats vom 28. Mai 1993, 2 BvF 2/90 u.a. "
            "(tzw. drugie orzeczenie aborcyjne). Dostęp: 24.12.2025, "
            "https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/1993/05/rs19930528_2bvf000290.html",
        ),
        Citation(
            4,
            "ETPCz, Tysiąc p. Polsce, skarga nr 5410/03, wyrok z 20.03.2007 (HUDOC). "
            "Dostęp: 24.12.2025, https://hudoc.echr.coe.int/eng?i=001-79812",
        ),
        Citation(
            5,
            "ETPCz, A., B. i C. p. Irlandii, skarga nr 25579/05, wyrok Wielkiej Izby z 16.12.2010 (HUDOC). "
            "Dostęp: 24.12.2025, https://hudoc.echr.coe.int/",
        ),
        Citation(
            6,
            "ETPCz, Vo p. Francji, skarga nr 53924/00, wyrok Wielkiej Izby z 08.07.2004 (HUDOC). "
            "Dostęp: 24.12.2025, https://hudoc.echr.coe.int/",
        ),
        Citation(
            7,
            "StGB § 218 (Abbruch der Schwangerschaft) – tekst dostępny w publicznym serwisie prawnym dejure.org "
            "(źródło pomocnicze; zalecana weryfikacja z oficjalnym serwisem Bundesministeriums der Justiz). "
            "Dostęp: 24.12.2025, https://dejure.org/gesetze/StGB/218.html",
        ),
        Citation(
            8,
            "StGB § 218a (Straflosigkeit des Schwangerschaftsabbruchs) – tekst dostępny w publicznym serwisie prawnym "
            "dejure.org (źródło pomocnicze; zalecana weryfikacja z oficjalnym serwisem Bundesministeriums der Justiz). "
            "Dostęp: 24.12.2025, https://dejure.org/gesetze/StGB/218a.html",
        ),
    ]

    doc = Document()

    # Basic typography (KISS; avoids complex templates).
    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)

    doc.add_paragraph("Temat pracy:")
    doc.add_paragraph(
        "Prawne regulacje przerwania ciąży w wybranych krajach Unii Europejskiej "
        "na przykładzie Malty, Niemiec i Holandii"
    )
    doc.add_paragraph(f"Data opracowania: {date.today().strftime('%d.%m.%Y')}")

    doc.add_page_break()

    doc.add_heading("Wstęp", level=1)
    _add_paragraph_with_citations(
        doc,
        [
            "Problematyka prawnej dopuszczalności przerwania ciąży pozostaje jednym z najbardziej "
            "spornych zagadnień współczesnego prawa publicznego i prawa medycznego. Spór ten ma charakter "
            "wielowymiarowy: dotyczy zarówno aksjologii konstytucyjnej (ochrona życia, godność człowieka), "
            "jak i praw jednostki (autonomia, prywatność), a zarazem funkcjonuje w praktycznym kontekście "
            "świadczeń zdrowotnych. Na tym tle państwa członkowskie Unii Europejskiej przyjęły modele "
            "regulacyjne o wyraźnie odmiennej intensywności ochrony życia prenatalnego oraz odmiennym "
            "rozumieniu roli państwa w podejmowaniu decyzji prokreacyjnych."
        ],
        citations=[6],
    )
    _add_paragraph_with_citations(
        doc,
        [
            "Celem niniejszej pracy (w części obejmującej wstęp oraz dwa pierwsze rozdziały) jest "
            "rekonstrukcja i analiza prawnych regulacji przerwania ciąży w trzech jurysdykcjach: "
            "na Malcie, w Niemczech oraz w Holandii, z uwzględnieniem genezy historycznej tych rozwiązań "
            "i ich osadzenia w standardach wynikających z orzecznictwa Europejskiego Trybunału Praw Człowieka "
            "(ETPCz). Dobór państw ma charakter celowy: Malta reprezentuje model restrykcyjny (z dominacją zakazu), "
            "Niemcy – model kompromisowy, oparty na konstrukcji bezprawności niepodlegającej karze w warunkach "
            "spełnienia określonych przesłanek, a Holandia – model liberalny, powiązany z kryterium przeżywalności "
            "płodu i rozbudowanymi standardami medycznymi."
        ],
        citations=[1, 2, 7, 8],
    )
    _add_paragraph_with_citations(
        doc,
        [
            "Praca ma charakter dogmatyczno-prawny, z wykorzystaniem metody porównawczej oraz elementów "
            "analizy historyczno-prawnej. W zakresie prawa międzynarodowego praw człowieka szczególne "
            "znaczenie przypisano standardom proceduralnym wypracowanym w judykaturze ETPCz, które – "
            "przy zachowaniu szerokiego marginesu oceny państw – wpływają na ocenę efektywności krajowych "
            "mechanizmów ochrony praw pacjentek i realizacji obowiązków państwa w obszarze ochrony zdrowia."
        ],
        citations=[4, 5],
    )
    _add_paragraph_with_citations(
        doc,
        [
            "W ramach przyjętej struktury Rozdział I przedstawia pojęcie i rozwój instytucji aborcji "
            "oraz czynniki kształtujące ewolucję prawa aborcyjnego w Europie, w tym krótką rekonstrukcję "
            "trajektorii zmian na Malcie, w Niemczech i w Holandii, a także rolę procesów integracji europejskiej "
            "oraz orzecznictwa strasburskiego. Rozdział II zawiera analizę obowiązujących regulacji prawnych "
            "w tych państwach, z podziałem na modele terminowe, przesłankowe i zakazowe, a także z uwzględnieniem "
            "znaczenia klauzuli sumienia dla dostępności świadczeń."
        ],
        citations=None,
    )

    doc.add_heading("Rozdział I. Pojęcie i rozwój instytucji aborcji", level=1)
    doc.add_heading(
        "1.1. Społeczno-kulturowe i religijne uwarunkowania ewolucji prawa aborcyjnego w Europie",
        level=2,
    )
    _add_paragraph_with_citations(
        doc,
        [
            "W europejskiej kulturze prawnej regulacja przerwania ciąży tradycyjnie pozostawała w ścisłym związku "
            "z dominującymi w danym społeczeństwie przekonaniami religijnymi i moralnymi, a w wymiarze prawnym – "
            "z ewolucją pojęć takich jak „życie ludzkie”, „osoba” czy „godność”. Z jednej strony, silny wpływ tradycji "
            "chrześcijańskiej sprzyjał modelom zakazowym oraz penalizacji aborcji jako czynu naruszającego wartość życia. "
            "Z drugiej, procesy sekularyzacji, emancypacji kobiet i rozwój praw pacjenta prowadziły do stopniowej "
            "depenalizacji bądź wprowadzania wyjątków, uzasadnianych ochroną zdrowia, sytuacją życiową kobiety albo "
            "ochroną przed skutkami przestępstwa. Równolegle, rozwój medycyny (diagnostyka prenatalna, pojęcie "
            "przeżywalności płodu) dostarczał ustawodawcom nowych punktów odniesienia dla granic dopuszczalności zabiegu."
        ],
        citations=[6],
    )
    _add_paragraph_with_citations(
        doc,
        [
            "Na poziomie europejskiego systemu ochrony praw człowieka ETPCz konsekwentnie wskazuje, że Konwencja "
            "nie ustanawia jednolitego modelu dopuszczalności aborcji, a państwa korzystają z szerokiego marginesu "
            "oceny w kształtowaniu norm materialnych. Jednocześnie Trybunał rozwinął wymagania proceduralne: "
            "jeżeli prawo krajowe dopuszcza aborcję w określonych okolicznościach, mechanizmy ich realizacji muszą być "
            "skuteczne, dostępne i zapewniać realną możliwość skorzystania z uprawnienia (m.in. w zakresie "
            "rozstrzygania sporów medycznych i terminowości działań)."
        ],
        citations=[4, 5],
    )

    doc.add_heading(
        "1.2. Od całkowitego zakazu do wąskiego wyjątku: historia prawnej ochrony życia poczętego na Malcie",
        level=2,
    )
    _add_paragraph_with_citations(
        doc,
        [
            "Malta przez dziesięciolecia należała do najbardziej restrykcyjnych jurysdykcji europejskich w zakresie "
            "aborcji. Model maltański opiera się na silnej penalizacji przerwania ciąży, ujmowanej jako przestępstwo "
            "przeciwko życiu i zdrowiu, z konsekwencjami zarówno dla kobiety, jak i osoby dokonującej zabiegu. "
            "Z perspektywy dogmatycznej istotne jest, że punkt ciężkości regulacji zlokalizowano w prawie karnym, "
            "co sprzyja tzw. efektowi mrożącemu w praktyce klinicznej (ryzyko odpowiedzialności przy stanach granicznych)."
        ],
        citations=[1],
    )
    _add_paragraph_with_citations(
        doc,
        [
            "W ostatnich latach obserwuje się jednak ostrożną ewolucję w kierunku dopuszczenia wąskiego wyjątku "
            "związanego z ochroną życia (a w ujęciu medycznym – również zdrowia) kobiety ciężarnej. Zmiany te należy "
            "interpretować nie jako przyjęcie modelu przesłankowego w znaczeniu klasycznym, lecz raczej jako próbę "
            "wyważenia aksjologii ochrony życia prenatalnego z obowiązkiem państwa zapewnienia minimalnego bezpieczeństwa "
            "medycznego w sytuacjach zagrożenia życia kobiety. W konsekwencji, w prawie maltańskim utrzymuje się "
            "dominacja zakazu, a wyjątek ma charakter wyjątkowo wąski i silnie sformalizowany."
        ],
        citations=[1],
    )

    doc.add_heading("1.3. Ewolucja modelu niemieckiego", level=2)
    _add_paragraph_with_citations(
        doc,
        [
            "Niemiecka regulacja przerwania ciąży stanowi przykład modelu kompromisowego, zakorzenionego w konstytucyjnej "
            "ochronie życia i godności, a zarazem uwzględniającego sytuację konfliktową kobiety ciężarnej. Kluczowe znaczenie "
            "ma orzecznictwo Federalnego Trybunału Konstytucyjnego, które – w ujęciu systemowym – traktuje ochronę życia "
            "prenatalnego jako obowiązek państwa (Schutzpflicht), wymagający stworzenia norm i instrumentów realnie "
            "chroniących to dobro. Jednocześnie w praktyce ustawodawczej wypracowano rozwiązania, które w określonych "
            "warunkach rezygnują z represji karnej, przesuwając akcent na poradnictwo i wsparcie socjalne."
        ],
        citations=[3],
    )
    _add_paragraph_with_citations(
        doc,
        [
            "W ujęciu dogmatycznym istotą niemieckiego modelu jest rozróżnienie pomiędzy bezprawnością czynu a jego "
            "karalnością: w typowych przypadkach aborcja pozostaje bezprawna, jednak ustawodawca przewiduje sytuacje, "
            "w których nie podlega karze (przede wszystkim przy spełnieniu przesłanek czasowych i proceduralnych "
            "związanych z obowiązkowym poradnictwem). Rozwiązanie to odzwierciedla napięcie pomiędzy aksjologią "
            "ochrony życia a wolą ograniczenia penalizacji w praktyce."
        ],
        citations=[7, 8, 3],
    )

    doc.add_heading("1.4. Geneza liberalizacji w Holandii", level=2)
    _add_paragraph_with_citations(
        doc,
        [
            "Holenderski model regulacyjny rozwijał się w odmiennym kontekście kulturowym i politycznym, w którym "
            "większy nacisk położono na autonomię jednostki i pragmatykę zdrowia publicznego. Ustawa o przerywaniu ciąży "
            "wyznacza granicę dopuszczalności zabiegu w oparciu o kryterium przeżywalności płodu poza organizmem matki "
            "(viability), a centralnym elementem jest konstrukcja „należytej staranności” w praktyce lekarskiej. "
            "W konsekwencji regulacja holenderska ma charakter w znacznym stopniu medykalizowany: przesłanki i procedury "
            "są powiązane z obowiązkami informacyjnymi, kwalifikacją podmiotów wykonujących zabieg oraz zapewnieniem "
            "standardów opieki."
        ],
        citations=[2],
    )

    doc.add_heading(
        "1.5. Wpływ procesów integracji europejskiej i orzecznictwa strasburskiego (ETPCz) na zmiany w prawie krajowym",
        level=2,
    )
    _add_paragraph_with_citations(
        doc,
        [
            "W ramach Unii Europejskiej brak jest pełnej harmonizacji materialnych przesłanek dopuszczalności aborcji, "
            "co sprzyja utrzymywaniu się dywergencji standardów pomiędzy państwami członkowskimi. Jednak integracja "
            "europejska oddziałuje pośrednio: przez swobody przepływu (w tym realną możliwość korzystania ze świadczeń "
            "zdrowotnych w innym państwie), przez standardy ochrony zdrowia oraz przez wzrost znaczenia praw pacjenta "
            "i zasad niedyskryminacji. Najbardziej namacalny wpływ na prawo krajowe wywiera jednak orzecznictwo ETPCz, "
            "które – nie rozstrzygając „kiedy zaczyna się życie” w sensie konwencyjnym – nakłada na państwa obowiązki "
            "zapewnienia spójnych i skutecznych procedur, jeżeli aborcja jest w danym systemie prawnie dopuszczalna."
        ],
        citations=[4, 5, 6],
    )

    doc.add_heading("Rozdział II. Regulacje prawne aborcji w państwach europejskich", level=1)
    doc.add_heading(
        "2.1. Systematyka modeli regulacyjnych w Unii Europejskiej: rozwiązania terminowe, przesłankowe i zakazowe",
        level=2,
    )
    _add_paragraph_with_citations(
        doc,
        [
            "Porównanie rozwiązań europejskich pozwala wyodrębnić trzy podstawowe typy modeli regulacyjnych. "
            "Po pierwsze, model terminowy dopuszcza aborcję do określonego etapu ciąży (np. do granicy przeżywalności), "
            "zwykle przy spełnieniu wymogów proceduralnych i wykonywaniu zabiegu przez uprawniony personel. "
            "Po drugie, model przesłankowy uzależnia dopuszczalność aborcji od wystąpienia wskazanych okoliczności "
            "(np. medycznych czy kryminologicznych), niezależnie od terminu lub z dodatkowymi ograniczeniami czasowymi. "
            "Po trzecie, model zakazowy opiera się na generalnej penalizacji, dopuszczając co najwyżej wąskie wyjątki "
            "związane z ratowaniem życia. W praktyce państwa często łączą elementy tych modeli, co widać szczególnie "
            "w rozwiązaniu niemieckim (zakaz + szerokie niekaranie w procedurze poradnictwa)."
        ],
        citations=[1, 2, 7, 8],
    )

    doc.add_heading(
        "2.2. Malta: analiza przepisów Kodeksu Karnego (art. 241–243) oraz zmian z 2023 r. w świetle ochrony życia matki",
        level=2,
    )
    _add_paragraph_with_citations(
        doc,
        [
            "Regulacja maltańska tradycyjnie przybiera postać penalizacji przerwania ciąży w Kodeksie karnym "
            "(Criminal Code). Konstrukcyjnie przestępstwo obejmuje zarówno zachowania osoby trzeciej dokonującej "
            "zabiegu, jak i udział kobiety w jego dokonaniu, co czyni prawo karne podstawowym instrumentem ochrony "
            "życia prenatalnego. W modelu tym ochrona życia poczętego ma charakter dominujący, a ustawodawca "
            "minimalizuje przestrzeń dla wyjątków."
        ],
        citations=[1],
    )
    _add_paragraph_with_citations(
        doc,
        [
            "W 2023 r. wprowadzono zmianę, której ratio legis przedstawiano jako zapewnienie bezpieczeństwa "
            "medycznego w sytuacjach zagrożenia życia kobiety. Z perspektywy dogmatycznej jest to istotne, "
            "ponieważ nawet w systemie zakazowym pojawia się potrzeba doprecyzowania granic stanu wyższej "
            "konieczności w medycynie, aby ograniczyć ryzyko zaniechania interwencji ratującej życie. "
            "W konsekwencji ocena maltańskiego modelu wymaga rozróżnienia: (a) utrzymania generalnej penalizacji "
            "aborcji oraz (b) wyodrębnienia wąskiego wyjątku w przypadkach bezpośredniego zagrożenia życia, "
            "który ma znaczenie przede wszystkim dla praktyki klinicznej i decyzji personelu medycznego."
        ],
        citations=[1],
    )

    doc.add_heading(
        "2.3. Niemcy: konstrukcja „bezprawności niepodlegającej karze” (straflos aber rechtswidrig) i system obowiązkowego poradnictwa",
        level=2,
    )
    _add_paragraph_with_citations(
        doc,
        [
            "W prawie niemieckim punkt wyjścia stanowi kryminalizacja aborcji w StGB. Jednocześnie ustawodawca "
            "przewiduje sytuacje niekaralności, które – w dyskursie prawniczym – bywają ujmowane jako „bezprawność "
            "niepodlegająca karze”. Rozwiązanie to ma doniosłe konsekwencje: państwo nie rezygnuje z aksjologicznego "
            "potępienia czynu, lecz odstępuje od represji pod warunkiem spełnienia ustawowych wymogów, które mają "
            "pełnić funkcję ochronną (w szczególności przez poradnictwo i upływ czasu)."
        ],
        citations=[7, 8],
    )
    _add_paragraph_with_citations(
        doc,
        [
            "Orzecznictwo BVerfG stanowi konstytucyjny fundament tej konstrukcji: Trybunał podkreśla obowiązek państwa "
            "ochrony życia prenatalnego, dopuszczając zarazem, aby instrumenty ochronne nie ograniczały się do sankcji "
            "karnych, lecz obejmowały środki prewencyjne i socjalne. W tym ujęciu poradnictwo ma charakter "
            "instytucjonalnego „kanału” realizacji ochrony życia, a nie jedynie formalnego wymogu."
        ],
        citations=[3],
    )

    doc.add_heading(
        "2.4. Holandia: prawne ramy aborcji na żądanie do momentu przeżywalności płodu (viability) i zniesienie obligatoryjnego okresu oczekiwania",
        level=2,
    )
    _add_paragraph_with_citations(
        doc,
        [
            "Holenderska ustawa WAZ konstruuje dopuszczalność przerwania ciąży w oparciu o kryterium przeżywalności "
            "płodu poza organizmem matki, które ma charakter dynamiczny i pozostaje powiązane z wiedzą medyczną. "
            "Ustawodawca kładzie nacisk na należyte poinformowanie pacjentki, rozważenie sytuacji oraz zapewnienie, "
            "że decyzja jest podjęta w sposób przemyślany. W efekcie centralnym punktem regulacji nie jest penalizacja, "
            "lecz wymogi staranności i organizacji świadczenia w systemie ochrony zdrowia."
        ],
        citations=[2],
    )
    _add_paragraph_with_citations(
        doc,
        [
            "W praktyce europejskiej szczególne znaczenie ma trend odchodzenia od sztywnych, obligatoryjnych okresów "
            "oczekiwania, zastępowanych elastyczniejszymi standardami informacyjnymi i konsultacyjnymi. W modelu "
            "holenderskim dyskusja ta wiąże się z oceną, czy ustawowy „czas do namysłu” rzeczywiście zwiększa "
            "autonomię decyzji, czy raczej tworzy barierę dostępu do świadczeń. Z perspektywy prawnoporównawczej "
            "to istotny element różnicujący Holandię i Niemcy, gdzie czas i poradnictwo pełnią także funkcję "
            "instrumentu ochrony życia prenatalnego."
        ],
        citations=[2, 7, 8],
    )

    doc.add_heading(
        "2.5. Status prawny klauzuli sumienia i jej wpływ na dostępność świadczeń w wybranych jurysdykcjach",
        level=2,
    )
    _add_paragraph_with_citations(
        doc,
        [
            "Klauzula sumienia stanowi mechanizm prawny mający chronić wolność sumienia osób wykonujących zawody "
            "medyczne, jednak jej zakres i warunki stosowania mogą istotnie wpływać na realną dostępność świadczeń. "
            "W ujęciu prawnoporównawczym istotne jest rozróżnienie pomiędzy: (a) prawem jednostkowego sprzeciwu "
            "konkretnego lekarza oraz (b) systemowymi obowiązkami państwa w zakresie organizacji opieki zdrowotnej. "
            "Nawet przy uznaniu sprzeciwu sumienia, państwo pozostaje zobowiązane do zapewnienia skutecznej ścieżki "
            "dostępu do świadczenia tam, gdzie jest ono legalne; w przeciwnym razie dochodzi do naruszenia standardów "
            "proceduralnych ochrony praw pacjentki."
        ],
        citations=[4, 5],
    )

    doc.add_page_break()
    doc.add_heading("Przypisy", level=1)
    for c in citations:
        p = doc.add_paragraph()
        n_run = p.add_run(f"{c.n}. ")
        n_run.bold = True
        p.add_run(c.text)

    return doc, citations


def main() -> None:
    doc, _ = build_document()
    output_path = "/workspace/paper/Wstep_Rozdzial_I_II_regulacje_aborcji_Malta_Niemcy_Holandia.docx"
    doc.save(output_path)
    print(output_path)


if __name__ == "__main__":
    main()

