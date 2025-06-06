from boinor.bodies import (
    Earth,
    Jupiter,
    Mars,
    Mercury,
    Neptune,
    Saturn,
    Sun,
    Uranus,
    Venus,
)
from boinor.constants import J2000
from boinor.frames.ecliptic import (
    GeocentricMeanEcliptic,
    HeliocentricEclipticJ2000,
)
from boinor.frames.enums import Planes
from boinor.frames.equatorial import (
    GCRS,
    HCRS,
    JupiterICRS,
    MarsICRS,
    MercuryICRS,
    NeptuneICRS,
    SaturnICRS,
    UranusICRS,
    VenusICRS,
)
from boinor.frames.fixed import (
    ITRS,
    JupiterFixed,
    MarsFixed,
    MercuryFixed,
    NeptuneFixed,
    SaturnFixed,
    UranusFixed,
    VenusFixed,
)

_FRAME_MAPPING = {
    Sun: {
        Planes.EARTH_EQUATOR: HCRS,
        Planes.EARTH_ECLIPTIC: HeliocentricEclipticJ2000,
    },
    Mercury: {
        Planes.EARTH_EQUATOR: MercuryICRS,
        Planes.BODY_FIXED: MercuryFixed,
    },
    Venus: {Planes.EARTH_EQUATOR: VenusICRS, Planes.BODY_FIXED: VenusFixed},
    Earth: {
        Planes.EARTH_EQUATOR: GCRS,
        Planes.EARTH_ECLIPTIC: GeocentricMeanEcliptic,
        Planes.BODY_FIXED: ITRS,
    },
    Mars: {Planes.EARTH_EQUATOR: MarsICRS, Planes.BODY_FIXED: MarsFixed},
    Jupiter: {
        Planes.EARTH_EQUATOR: JupiterICRS,
        Planes.BODY_FIXED: JupiterFixed,
    },
    Saturn: {Planes.EARTH_EQUATOR: SaturnICRS, Planes.BODY_FIXED: SaturnFixed},
    Uranus: {Planes.EARTH_EQUATOR: UranusICRS, Planes.BODY_FIXED: UranusFixed},
    Neptune: {
        Planes.EARTH_EQUATOR: NeptuneICRS,
        Planes.BODY_FIXED: NeptuneFixed,
    },
}  # type: Dict[Union[Body, SolarSystemPlanet], Dict[Planes, BaseCoordinateFrame]]


def get_frame(attractor, plane, obstime=J2000):
    """Returns an appropriate reference frame from an attractor and a plane.

    Available planes are Earth equator (parallel to GCRS) and Earth ecliptic.
    The fundamental direction of both is the equinox of epoch (J2000).
    An obstime is needed to properly locate the attractor.

    Parameters
    ----------
    attractor : ~boinor.bodies.Body
        Body that serves as the center of the frame.
    plane : ~boinor.frames.Planes
        Fundamental plane of the frame.
    obstime : ~astropy.time.Time
        Time of the frame.

    """
    try:
        frames = _FRAME_MAPPING[attractor]
    except KeyError as e:
        raise NotImplementedError(
            "Frames for orbits around custom bodies are not yet supported"
        ) from e

    try:
        frame_class = frames[plane]
    except KeyError as e:
        raise NotImplementedError(
            f"A frame with plane {plane} around body {attractor} is not yet implemented"
        ) from e

    return frame_class(obstime=obstime)
