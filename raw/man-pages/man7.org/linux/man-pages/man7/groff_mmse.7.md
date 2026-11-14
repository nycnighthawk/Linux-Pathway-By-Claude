---
{"title": "groff_mmse(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/groff_mmse.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# groff_mmse(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [Namn](#Namn) \| [Syntax](#Syntax) \| [Beskrivning](#Beskrivning) \| [Brev](#Brev) \| [Skrivet av](#Skrivet_av) \| [Filer](#Filer) \| [Se också](#Se_också) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    groff_mmse(7)        Miscellaneous Information Manual       groff_mmse(7)

## [](#Namn)Namn

           groff_mmse - svenska ”memorandum” makro för GNU roff

## [](#Syntax)Syntax

           groff -mmse [flaggor ...] [filer ...]

           groff -m mmse [flaggor ...] [filer ...]

## [](#Beskrivning)Beskrivning

           mmse är en svensk variant av mm.  Alla texter är översatta.  En A4
           sida får text som är 13 cm bred, 3,5 cm indragning samt är 28,5 cm
           hög.  Det finns stöd för brevuppställning enligt svensk standard
           för vänster och högerjusterad text.

           COVER kan använda se_ms som argument.  Detta ger ett svenskt
           försättsblad.  Se groff_mm(7) för övriga detaljer.

## [](#Brev)Brev

           Tillgängliga brevtyper:

           .LT SVV
                  Vänsterställd löptext med adressat i position T0
                  (vänsterställt).

           .LT SVH
                  Högerställd löptext med adressat i position T4 (passar
                  fönsterkuvert).

           Följande extra LO-variabler används.

           .LO DNAMN namn
                  Anger dokumentets namn.

           .LO MDAT datum
                  Mottagarens datum, anges under Ert datum: (LetMDAT).

           .LO BIL sträng
                  Anger bilaga, nummer eller sträng med Bilaga (LetBIL) som
                  prefix.

           .LO KOMP text
                  Anger kompletteringsuppgift.

           .LO DBET beteckning
                  Anger dokumentbeteckning eller dokumentnummer.

           .LO BET beteckning
                  Anger beteckning (ärendebeteckning i form av diarienummer
                  eller liknande).

           .LO SIDOR antal
                  Anger totala antalet sidor och skrivs ut efter sidnumret
                  inom parenteser.

           Om makrot .TP är definierat anropas det efter utskrift av
           brevhuvudet.  Där lägger man lämpligen in postadress och annat som
           brevfot.

## [](#Skrivet_av)Skrivet av

           Jörgen Hägg ⟨Jorgen.Hagg@axis.se⟩, Lund, Sweden

## [](#Filer)Filer

           /usr/local/share/groff/1.24.1/tmac/mse.tmac

           /usr/local/share/groff/1.24.1/tmac/mm/se_*.cov

## [](#Se_också)Se också

           groff_mm(7)

## [](#COLOPHON)COLOPHON

           This page is part of the groff (GNU troff) project.  Information
           about the project can be found at 
           ⟨http://www.gnu.org/software/groff/⟩.  If you have a bug report for
           this manual page, see ⟨http://www.gnu.org/software/groff/⟩.  This
           page was obtained from the tarball groff-1.24.1.tar.gz fetched
           from ⟨https://ftp.gnu.org/gnu/groff/⟩ on 2026-08-04.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    groff 1.24.1                    2026-03-14                  groff_mmse(7)

------------------------------------------------------------------------

------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+
| HTML rendering created 2026-09-09 by [Michael Kerrisk](https://man7.org/mtk/index.html), author of [*The Linux Programming Interface*](https://man7.org/tlpi/). |                       | [](https://man7.org/tlpi/) |
|                                                                                                                                                                 |                       |                            |
| For details of in-depth **Linux/UNIX system programming training courses** that I teach, look [here](https://man7.org/training/).                               |                       |                            |
|                                                                                                                                                                 |                       |                            |
| Hosting by [jambit GmbH](https://www.jambit.com/index_en.html).                                                                                                 |                       |                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+----------------------------+

------------------------------------------------------------------------
