---
{"title": "Codecs and containers", "url": "https://wiki.archlinux.org/title/Codecs_and_containers", "retrieved": "2026-11-01", "license": "GFDL-1.3-or-later"}
---

# Codecs and containers

Related articles

-   [Optical disc drive#Playback](../en/Optical_disc_drive.html#Playback "Optical disc drive")
-   [GStreamer](../en/GStreamer.html "GStreamer")
-   [FFmpeg](../en/FFmpeg.html "FFmpeg")

From [Wikipedia](https://en.wikipedia.org/wiki/Codec "wikipedia:Codec"):

A codec is a computer hardware or software component that encodes or decodes a data stream or signal.

In general, codecs are utilized by multimedia applications to encode or decode audio or video streams. In order to play encoded streams, users must ensure an appropriate codec is installed.

This article deals only with codecs and application backends; see [List of applications/Multimedia](../en/List_of_applications/Multimedia.html "List of applications/Multimedia") for a list of media players ([MPlayer](../en/MPlayer.html "MPlayer"), [mpv](../en/Mpv.html "Mpv") and [VLC](../en/VLC_media_player.html "VLC") are popular choices).

## Requirements {#Requirements}

Playing multimedia content requires two components:

-   A capable media player
-   The appropriate codec

It is not always necessary to explicitly install codecs if you have installed a media player. For example, [MPlayer](../en/MPlayer.html "MPlayer") pulls in a large number of codecs as dependencies, and also has codecs built in.

## List of codecs {#List_of_codecs}

**Note** Unlike the community repositories of *Fedora Linux*, *Arch Linux* does not distribute \"freeworld\" package variants for video and audio codecs protected by patents (such as in the [Mesa](../en/OpenGL.html "OpenGL") packages); the standard packages are compiled with all relevant codecs, like the \"freeworld\" ones from *Fedora*.

### Audio {#Audio}

See also [Wikipedia:Comparison of audio coding formats](https://en.wikipedia.org/wiki/Comparison_of_audio_coding_formats "wikipedia:Comparison of audio coding formats").

#### Lossless audio codecs {#Lossless_audio_codecs}

-   **[Apple Lossless](https://en.wikipedia.org/wiki/Apple_Lossless "wikipedia:Apple Lossless") (ALAC)** --- A lossless audio compression codec developed by Apple and deployed on all of its platforms and devices.

[https://alac.macosforge.org/](https://alac.macosforge.org/) \|\| [alac-git](https://aur.archlinux.org/packages/alac-git/)^AUR^

-   **[FLAC](https://en.wikipedia.org/wiki/FLAC "wikipedia:FLAC")** --- Free Lossless Audio Codec.

[https://xiph.org/flac/](https://xiph.org/flac/) \|\| [flac](https://archlinux.org/packages/?name=flac)

-   **[WavPack](https://en.wikipedia.org/wiki/WavPack "wikipedia:WavPack")** --- Lossless audio compression format that also has a lossy [hybrid mode](https://en.wikipedia.org/wiki/WavPack#Hybrid_mode "wikipedia:WavPack").

[https://www.wavpack.com/](https://www.wavpack.com/) \|\| [wavpack](https://archlinux.org/packages/?name=wavpack)

#### Lossy audio codecs {#Lossy_audio_codecs}

  ------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------- ------------------------------------------------------------- -------------------------------------------------------
  Format                                                                                                                                                                                 Encode                                                        Decode
  [AAC](https://en.wikipedia.org/wiki/Advanced_Audio_Coding "wikipedia:Advanced Audio Coding")                       [#AAC](#AAC)                                                                                                                      
  [ATSC A/52](https://en.wikipedia.org/wiki/ATSC_A/52 "wikipedia:ATSC A/52")                                         [aften](https://aur.archlinux.org/packages/aften/)^AUR^             [a52dec](https://archlinux.org/packages/?name=a52dec)         
  [CELT](https://en.wikipedia.org/wiki/CELT "wikipedia:CELT")                                                        [celt](https://aur.archlinux.org/packages/celt/)^AUR^                                                                             
  [MPEG-1](https://en.wikipedia.org/wiki/MPEG-1 "wikipedia:MPEG-1")                                                                                                                                                                                    [libmad](https://archlinux.org/packages/?name=libmad)
                                                                                                                     [MP3](https://en.wikipedia.org/wiki/MP3 "wikipedia:MP3")            [lame](https://archlinux.org/packages/?name=lame)             
  [Musepack](https://en.wikipedia.org/wiki/Musepack "wikipedia:Musepack") (MPC)                                      -- ^1^                                                              [libmpcdec](https://archlinux.org/packages/?name=libmpcdec)   
  [Opus](https://en.wikipedia.org/wiki/Opus_(audio_format) "wikipedia:Opus (audio format)")                          [opus](https://archlinux.org/packages/?name=opus)                                                                                 
  [Vorbis](https://en.wikipedia.org/wiki/Vorbis "wikipedia:Vorbis")                                                  [libvorbis](https://archlinux.org/packages/?name=libvorbis)                                                                       
  Speech codecs                                                                                                                                                                                                                                        
  [AMR](https://en.wikipedia.org/wiki/Adaptive_Multi-Rate_audio_codec "wikipedia:Adaptive Multi-Rate audio codec")   [opencore-amr](https://archlinux.org/packages/?name=opencore-amr)                                                                 
  [Speex](https://en.wikipedia.org/wiki/Speex "wikipedia:Speex")                                                     [speex](https://archlinux.org/packages/?name=speex)                                                                               
  ------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------- ------------------------------------------------------------- -------------------------------------------------------

1.  mppenc is not packaged.

-   **[CELT](https://en.wikipedia.org/wiki/CELT "wikipedia:CELT")** --- Open, royalty-free lossy audio codec, optimized for low latency.

[https://www.celt-codec.org/](https://www.celt-codec.org/) \|\| [celt](https://aur.archlinux.org/packages/celt/)^AUR^

-   **[LAME](https://en.wikipedia.org/wiki/LAME "wikipedia:LAME")** --- MP3 encoder and graphical frame analyzer.

[https://lame.sourceforge.io/](https://lame.sourceforge.io/) \|\| [lame](https://archlinux.org/packages/?name=lame)

-   **liba52** --- Free library for decoding [ATSC A/52](https://en.wikipedia.org/wiki/ATSC_A/52 "wikipedia:ATSC A/52") (Dolby Digital) streams (lossy).

[https://liba52.sourceforge.io/](https://liba52.sourceforge.io/) \|\| [a52dec](https://archlinux.org/packages/?name=a52dec)

-   **[libdca](https://en.wikipedia.org/wiki/libdca "wikipedia:libdca")** --- Free library for decoding DTS Coherent Acoustics streams.

[https://www.videolan.org/developers/libdca.html](https://www.videolan.org/developers/libdca.html) \|\| [libdca](https://archlinux.org/packages/?name=libdca)

-   **[MAD](https://en.wikipedia.org/wiki/libmad "wikipedia:libmad")** --- High-quality MPEG audio decoder.

[https://www.underbit.com/products/mad/](https://www.underbit.com/products/mad/) \|\| [libmad](https://archlinux.org/packages/?name=libmad)

-   **[Musepack](https://en.wikipedia.org/wiki/Musepack "wikipedia:Musepack") (MPC)** --- Open source lossy audio codec, designed for [transparency](https://en.wikipedia.org/wiki/Transparency_(data_compression) "wikipedia:Transparency (data compression)").

[https://musepack.net/](https://musepack.net/) \|\| [libmpcdec](https://archlinux.org/packages/?name=libmpcdec)

-   **[opencore-amr](https://en.wikipedia.org/wiki/Adaptive_Multi-Rate_audio_codec "wikipedia:Adaptive Multi-Rate audio codec")** --- Open source implementation of the Adaptive Multi Rate (AMR) speech codec.

[https://sourceforge.net/projects/opencore-amr/](https://sourceforge.net/projects/opencore-amr/) \|\| [opencore-amr](https://archlinux.org/packages/?name=opencore-amr)

-   **[Opus](https://en.wikipedia.org/wiki/Opus_(audio_codec) "wikipedia:Opus (audio codec)")** --- Open, royalty-free, lossy audio codec, designed for speech and general audio coding and low latency.

[https://www.opus-codec.org/](https://www.opus-codec.org/) \|\| [opus](https://archlinux.org/packages/?name=opus)

-   **[Speex](https://en.wikipedia.org/wiki/Speex "wikipedia:Speex")** --- Patent-free, lossy audio compression format designed for speech.

[https://www.speex.org/](https://www.speex.org/) \|\| [speex](https://archlinux.org/packages/?name=speex)

-   **[Vorbis](https://en.wikipedia.org/wiki/Vorbis "wikipedia:Vorbis")** --- Open, patent-free, lossy audio codec.

[https://xiph.org/vorbis/](https://xiph.org/vorbis/) \|\| [libvorbis](https://archlinux.org/packages/?name=libvorbis)

##### AAC {#AAC}

From [Wikipedia](https://en.wikipedia.org/wiki/Advanced_Audio_Coding "wikipedia:Advanced Audio Coding"):

**Advanced Audio Coding** (AAC) is a proprietary audio coding standard for lossy digital audio compression. Designed to be the successor of the MP3 format, AAC generally achieves better sound quality than MP3 at the same bit rate.

-   **[FAAC](https://en.wikipedia.org/wiki/FAAC "wikipedia:FAAC")** --- Proprietary AAC audio encoder.

[https://faac.sourceforge.net/](https://faac.sourceforge.net/) \|\| [faac](https://archlinux.org/packages/?name=faac)

-   **[FAAD2](https://en.wikipedia.org/wiki/FAAD2 "wikipedia:FAAD2")** --- ISO AAC audio decoder.

[https://faac.sourceforge.net/](https://faac.sourceforge.net/) \|\| [faad2](https://archlinux.org/packages/?name=faad2)

-   **[Fraunhofer FDK AAC](https://en.wikipedia.org/wiki/Fraunhofer_FDK_AAC "wikipedia:Fraunhofer FDK AAC")** --- OpenCORE Framework implementation Advanced Audio Coding (AAC) encoder. Modified library of Fraunhofer AAC decoder and encoder.

[https://sourceforge.net/projects/opencore-amr/](https://sourceforge.net/projects/opencore-amr/) \|\| [libfdk-aac](https://archlinux.org/packages/?name=libfdk-aac) (codec library) [fdkaac](https://archlinux.org/packages/?name=fdkaac) (CLI frontend for libfdk-aac)

-   **[Nero AAC](https://en.wikipedia.org/wiki/Nero_AAC_Codec "wikipedia:Nero AAC Codec")** --- Nero AAC reference quality MPEG-4 and 3GPP audio codec. (deprecated)

[https://www.nero.com/](https://www.nero.com/) \|\| [neroaac-bin](https://aur.archlinux.org/pkgbase/neroaac-bin/)^AUR^

### Image codecs {#Image_codecs}

-   **[JasPer](https://en.wikipedia.org/wiki/JasPer "wikipedia:JasPer")** --- Software-based implementation of the codec specified in the emerging JPEG-2000 Part-1 standard.

[https://www.ece.uvic.ca/\~frodo/jasper/](https://www.ece.uvic.ca/~frodo/jasper/) \|\| [jasper](https://archlinux.org/packages/?name=jasper)

-   **[OpenJPEG](https://en.wikipedia.org/wiki/OpenJPEG "wikipedia:OpenJPEG")** --- Open source JPEG 2000 codec.

[https://www.openjpeg.org/](https://www.openjpeg.org/) \|\| [openjpeg](https://aur.archlinux.org/packages/openjpeg/)^AUR^

-   **[WebP](https://en.wikipedia.org/wiki/WebP "wikipedia:WebP")** --- An image format employing both lossy and lossless compression. It is currently developed by Google.

[https://developers.google.com/speed/webp/](https://developers.google.com/speed/webp/) \|\| [libwebp](https://archlinux.org/packages/?name=libwebp)

-   **[AV1 Image File Format (AVIF)](https://en.wikipedia.org/wiki/AVIF "wikipedia:AVIF")** --- Image format based on the AV1 video codec.

[https://github.com/AOMediaCodec/libavif](https://github.com/AOMediaCodec/libavif) \|\| [libavif](https://archlinux.org/packages/?name=libavif)

-   **[High Efficiency Image File Format (HEIF)](https://en.wikipedia.org/wiki/High_Efficiency_Image_File_Format "wikipedia:High Efficiency Image File Format")** --- Image format based on the HEVC video codec. Often in a HEIC container.

[https://github.com/strukturag/libheif](https://github.com/strukturag/libheif) \|\| [libheif](https://archlinux.org/packages/?name=libheif)

-   **[JPEG XL](https://en.wikipedia.org/wiki/JPEG_XL "wikipedia:JPEG XL")** --- Royalty-free image format developed by the Joint Photographic Experts Group which aims for broad usage, capable of re-encoding JPEGs while avoiding generation loss.

[https://jpeg.org/jpegxl/](https://jpeg.org/jpegxl/) \|\| [libjxl](https://archlinux.org/packages/?name=libjxl)

### Video codecs {#Video_codecs}

See also [Wikipedia:Comparison of video codecs](https://en.wikipedia.org/wiki/Comparison_of_video_codecs "wikipedia:Comparison of video codecs").

  ---------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Format                                                                                                                 Codec Libraries
  [AV1](https://en.wikipedia.org/wiki/AV1 "wikipedia:AV1")                                                               [aom](https://archlinux.org/packages/?name=aom), [dav1d](https://archlinux.org/packages/?name=dav1d) (decode), [rav1e](https://archlinux.org/packages/?name=rav1e) (encode), [svt-av1](https://archlinux.org/packages/?name=svt-av1)
  [AVS2](https://en.wikipedia.org/wiki/Audio_Video_Standard "wikipedia:Audio Video Standard")                            [davs2](https://aur.archlinux.org/packages/davs2/)^AUR^ (decode)
  [Daala](https://en.wikipedia.org/wiki/Daala "wikipedia:Daala")                                                         [daala-git](https://aur.archlinux.org/packages/daala-git/)^AUR^
  [Dirac](https://en.wikipedia.org/wiki/Dirac_(video_compression_format) "wikipedia:Dirac (video compression format)")   [schroedinger](https://archlinux.org/packages/?name=schroedinger)
  [DV](https://en.wikipedia.org/wiki/DV "wikipedia:DV")                                                                  [libdv](https://archlinux.org/packages/?name=libdv)
  [H.265](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding "wikipedia:High Efficiency Video Coding")           [x265](https://archlinux.org/packages/?name=x265)
                                                                                                                         [libde265](https://archlinux.org/packages/?name=libde265)
  [H.264](https://en.wikipedia.org/wiki/H.264 "wikipedia:H.264")                                                         [x264](https://archlinux.org/packages/?name=x264)
  [MPEG-1](https://en.wikipedia.org/wiki/MPEG-1 "wikipedia:MPEG-1")                                                      [libmpeg2](https://archlinux.org/packages/?name=libmpeg2) (decode)
  [MPEG-2](https://en.wikipedia.org/wiki/MPEG-2 "wikipedia:MPEG-2")                                                      
  [MPEG-4](https://en.wikipedia.org/wiki/MPEG-4 "wikipedia:MPEG-4")                                                      [Xvid](https://en.wikipedia.org/wiki/Xvid "wikipedia:Xvid") ([xvidcore](https://archlinux.org/packages/?name=xvidcore))
  [Theora](https://en.wikipedia.org/wiki/Theora "wikipedia:Theora")                                                      [libtheora](https://archlinux.org/packages/?name=libtheora)
  [VP8](https://en.wikipedia.org/wiki/VP8 "wikipedia:VP8"), [VP9](https://en.wikipedia.org/wiki/VP9 "wikipedia:VP9")     [libvpx](https://archlinux.org/packages/?name=libvpx)
  ---------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   **[AV1](https://en.wikipedia.org/wiki/AV1 "wikipedia:AV1")** --- AOMedia Video 1 (AV1) is a successor codec to Google\'s VP9, Mozilla\'s Daala, Cisco\'s Thor. *aom* is the reference implementation of both encoding and decoding. *dav1d* is the performance focused decoder. *rav1e* is performance focused encoder. Most benchmark show better performances with svt-av1 than rav1e.

[https://aomediacodec.github.io/av1-spec/](https://aomediacodec.github.io/av1-spec/) \|\| [aom](https://archlinux.org/packages/?name=aom), [dav1d](https://archlinux.org/packages/?name=dav1d), [rav1e](https://archlinux.org/packages/?name=rav1e), [svt-av1](https://archlinux.org/packages/?name=svt-av1)

-   **[Daala](https://en.wikipedia.org/wiki/Daala "wikipedia:Daala")** --- Research video codec under development by the Xiph.Org Foundation and sponsored by the Mozilla Foundation. The goal of the project is to provide a free to implement, use and distribute digital media format and reference implementation with technical performance superior to h.265.

[https://www.xiph.org/daala/](https://www.xiph.org/daala/) \|\| [daala-git](https://aur.archlinux.org/packages/daala-git/)^AUR^

-   **libde265** --- Open source implementation of the h.265 video codec.

[https://github.com/strukturag/libde265](https://github.com/strukturag/libde265) \|\| [libde265](https://archlinux.org/packages/?name=libde265)

-   **[libdv](https://en.wikipedia.org/wiki/DV "wikipedia:DV")** --- The Quasar DV codec (libdv) is a software codec for DV video.

[https://libdv.sourceforge.net/](https://libdv.sourceforge.net/) \|\| [libdv](https://archlinux.org/packages/?name=libdv)

-   **[libmpeg2](https://en.wikipedia.org/wiki/libmpeg2 "wikipedia:libmpeg2")** --- Library for decoding MPEG-1 and MPEG-2 video streams.

[https://libmpeg2.sourceforge.io/](https://libmpeg2.sourceforge.io/) \|\| [libmpeg2](https://archlinux.org/packages/?name=libmpeg2)

-   **[Schrödinger](https://en.wikipedia.org/wiki/Dirac_(video_compression_format) "wikipedia:Dirac (video compression format)")** --- Advanced royalty-free video compression format designed for a wide range of uses, from delivering low-resolution web content to broadcasting HD and beyond, to near-lossless studio editing.

[https://launchpad.net/schroedinger/](https://launchpad.net/schroedinger/) \|\| [schroedinger](https://archlinux.org/packages/?name=schroedinger)

-   **[Theora](https://en.wikipedia.org/wiki/Theora "wikipedia:Theora")** --- Open video codec developed by the Xiph.org.

[https://www.theora.org/](https://www.theora.org/) \|\| [libtheora](https://archlinux.org/packages/?name=libtheora)

-   **[VP9](https://en.wikipedia.org/wiki/VP9 "wikipedia:VP9")** --- High-quality, open video format for the web that\'s freely available to everyone. Improved version of earlier [VP8](https://en.wikipedia.org/wiki/VP8 "wikipedia:VP8") codec.

[https://www.webmproject.org](https://www.webmproject.org) \|\| [libvpx](https://archlinux.org/packages/?name=libvpx)

-   **[x264](https://en.wikipedia.org/wiki/x264 "wikipedia:x264")** --- Free library for encoding H264/AVC video streams.

[https://www.videolan.org/developers/x264.html](https://www.videolan.org/developers/x264.html) \|\| [x264](https://archlinux.org/packages/?name=x264)

-   **[x265](https://en.wikipedia.org/wiki/x265 "wikipedia:x265")** --- Open-source project and free application library for encoding video streams into the H.265/High Efficiency Video Coding (HEVC) format.

[https://www.x265.org/](https://www.x265.org/) \|\| [x265](https://archlinux.org/packages/?name=x265)

-   **[Xvid](https://en.wikipedia.org/wiki/Xvid "wikipedia:Xvid")** --- Open source MPEG-4 video codec.

[https://www.xvid.com/](https://www.xvid.com/) \|\| [xvidcore](https://archlinux.org/packages/?name=xvidcore)

## Container format tools {#Container_format_tools}

See also [Wikipedia:Comparison of video container formats](https://en.wikipedia.org/wiki/Comparison_of_video_container_formats "wikipedia:Comparison of video container formats").

-   **[MKVToolNix](https://en.wikipedia.org/wiki/MKVToolNix "wikipedia:MKVToolNix")** --- Set of tools to create, edit and inspect Matroska files.

[https://mkvtoolnix.download/](https://mkvtoolnix.download/) \|\| [mkvtoolnix-cli](https://archlinux.org/packages/?name=mkvtoolnix-cli), [mkvtoolnix-gui](https://archlinux.org/packages/?name=mkvtoolnix-gui)

-   **MP4Joiner** --- A collection of GUI tools to manipulate MP4 files (MP4Joiner, MP4Splitter).

[https://www.mp4joiner.org/](https://www.mp4joiner.org/) \|\| [mp4joiner](https://aur.archlinux.org/packages/mp4joiner/)^AUR^

-   **OGMtools** --- Information, extraction or creation for OGG media streams.

[https://www.bunkus.org/videotools/ogmtools](https://www.bunkus.org/videotools/ogmtools) \|\| [ogmtools](https://archlinux.org/packages/?name=ogmtools)

## Backends {#Backends}

### GStreamer {#GStreamer}

From [https://gstreamer.freedesktop.org/](https://gstreamer.freedesktop.org/):

GStreamer is a library for constructing graphs of media-handling components. The applications it supports range from simple Ogg/Vorbis playback, audio/video streaming to complex audio (mixing) and video (non-linear editing) processing.

Simply, GStreamer is a *backend* or *framework* utilized by many media applications. See [GStreamer](../en/GStreamer.html "GStreamer") article.

### xine

From [https://sourceforge.net/projects/xine/](https://sourceforge.net/projects/xine/):

xine is a free multimedia player. It plays back CDs, DVDs, BluRays and VCDs. It also decodes multimedia files like AVI, MOV, WMV, and MP3 from local disk drives, and displays multimedia streamed over the Internet.

As an alternative to GStreamer, many media players can be configured to utilize the xine backend provided by [xine-lib](https://archlinux.org/packages/?name=xine-lib).

Note that the xine project itself provides a capable video player, [xine-ui](https://archlinux.org/packages/?name=xine-ui).

### libavcodec

[libavcodec](https://ffmpeg.org/libavcodec.html) is part of the [FFmpeg](../en/FFmpeg.html "FFmpeg") project. It includes a large number of video and audio codecs. The libavcodec codecs are included with media players such as [MPlayer](../en/MPlayer.html "MPlayer") and [VLC](../en/VLC_media_player.html "VLC"), so you may not need to install the [ffmpeg](https://archlinux.org/packages/?name=ffmpeg) package itself.

## Tips and tricks {#Tips_and_tricks}

### No H264, mpg4 or Musepack (.mpc) in Totem Player {#No_H264,_mpg4_or_Musepack_(.mpc)_in_Totem_Player}

If you see the \"The H264 plugin is missing\" warning with Totem media player, [install](../en/Help:Reading.html#Installation_of_packages "Install") [gst-libav](https://archlinux.org/packages/?name=gst-libav).

### No H264 in Parole Player {#No_H264_in_Parole_Player}

If you see the \"Parole needs H.264 decoder to play this file\" warning with Parole media player, [install](../en/Help:Reading.html#Installation_of_packages "Install") [gst-libav](https://archlinux.org/packages/?name=gst-libav).

### No H.264 in VLC {#No_H.264_in_VLC}

If you see the warning `VLC could not decode the format "h264" (H264 - MPEG-4 AVC (part 10))` [install](../en/Help:Reading.html#Installation_of_packages "Install") [vlc-plugin-ffmpeg](https://archlinux.org/packages/?name=vlc-plugin-ffmpeg).
